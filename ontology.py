import rdflib
from constants import classes_and_props_query, relations_query, create_mappings
from py2neo import Graph
import requests
import re
import pandas as pd
import asyncio
import aiohttp
import aiofiles
from aiohttp import BasicAuth
from py2neo import Graph
from datetime import date
import os

async def fetch_rdf_data(session, url, auth):
    try:
        async with session.get(url, auth=auth) as response:
            if response.status == 200:
                return await response.text()
            else:
                print(f"Node couldn't be exported, Error: {response.status}")
                return None
    except aiohttp.ClientConnectorError as e:
        print(f"Connection error: {e}")
        return None


async def process_batch(batch, prefix_mappings, auth, export_type):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for result in batch:
            # for local
            url = f"http://localhost:7474/rdf/neo4j/describe/{result['ID']}?format={export_type}"
            tasks.append(fetch_rdf_data(session, url, auth))

        responses = await asyncio.gather(*tasks)
        batch_rdf_data = []  # Collect all RDF data in a batch

        for i, rdf_data in enumerate(responses):
            node = batch[i]['ID']

            if rdf_data:
                # Replace the prefixes
                for old_prefix, new_prefix in prefix_mappings.items():
                    rdf_data = rdf_data.replace(old_prefix, new_prefix)

                # remove nan values 
                if export_type in "Turtle":
                    rdf_lines = rdf_data.split("\n")
                    new_lines = []
                    for line in rdf_lines:
                        if ("NaN" not in line):
                            new_lines.append(line)
                        else:
                            if line.endswith('.') and line.startswith("  sockg:"):
                                previous_line = new_lines.pop()
                                previous_line = previous_line[:-1] + '.'
                                new_lines.append(previous_line)

                    rdf_data = "\n".join(new_lines)
                else:
                    rdf_lines = rdf_data.split("\n")
                    rdf_lines = [line for line in rdf_lines if "NaN" not in line]
                    rdf_data = "\n".join(rdf_lines)

                if i == 0 and batch[0]['ID'] == 0:
                    # First write (include full RDF data)
                    if export_type == "RDF/XML":
                        rdf_data = "\n".join(rdf_data.split("\n")[:-1])
                        batch_rdf_data.append(rdf_data + "\n")
                    else:
                        batch_rdf_data.append(rdf_data + "\n")
                else:
                    # Skip the lines (header and prefix declarations) not needed
                    if export_type == "RDF/XML":
                        rdf_data = "\n".join(rdf_data.split("\n")[5:-1])
                        batch_rdf_data.append(rdf_data + "\n")
                    else:
                        rdf_data = "\n".join(rdf_data.split("\n")[2:])
                        batch_rdf_data.append(rdf_data + "\n")
                        



    # Return the RDF data to be written 
    return batch_rdf_data


async def rdf_query():
    username = input("Username: ")
    password = input("Password: ")

    try:
        auth = BasicAuth(username, password)  # Use BasicAuth for aiohttp
        graph = Graph("bolt://localhost:7687", auth=(username, password))
    except Exception as e:
        print(f"Couldn't connect to the Neo4j database: {e}")
        return

    node_count_query = "MATCH (n) RETURN count(n) AS node_count"

    node_count = graph.run(node_count_query).data()[0]['node_count']
    total_count = node_count 

    export_type = input("Enter the export type (N-Triples, RDF/XML, Turtle, JSON-LD): ")
    filename = f"sockg_{date.today()}"
    match export_type:
        case "N-Triples":
            filename += ".nt"
            filetype = ".nt"
        case "RDF/XML":
            filename += ".rdf"
            filetype = ".rdf"
        case "Turtle":
            filename += ".ttl"
            filetype = ".ttl"
        case "JSON-LD":
            filename += ".jsonld"
            filetype = ".jsonld"
        case _:                 
            filename += ".rdf"  # default is turtle
            filetype = ".rdf"

    current_exported_data_amount = 0
    batch_size = 2051  # 1024*3

    # for Turtle
    prefix_mappings = {
        'n4sch: <neo4j://graph.schema#>': 'sockg: <http://www.semanticweb.org/sockg/ontologies/2024/0/soil-carbon-ontology/>',
        'n4ind': 'sockg-n4ind',
        'n4sch': 'sockg',
    }

    # Clear the output file before writing
    async with aiofiles.open(f"output_files/{filename}", "w") as f:
        await f.write("")
        print(f"created output_files/{filename}")

    for file in os.listdir("output_files/"):
        if file.endswith(filetype):
            os.remove("output_files/" + file)

    while current_exported_data_amount < total_count:
        # Display progress (adjust progress calculation if needed)

        # Fetch the next batch of nodes
        query = f"MATCH (n) RETURN DISTINCT ID(n) as ID SKIP {current_exported_data_amount} LIMIT {batch_size}"
        results = graph.run(query).data()

        # Process the batch and get the RDF data
        batch_rdf_data = await process_batch(results, prefix_mappings, auth, export_type)

        # Write the batch RDF data to the file
        async with aiofiles.open(f"output_files/{filename}", "a") as f:
            await f.writelines(batch_rdf_data)

        # Update the progress
        current_exported_data_amount += len(results)
        progress = (current_exported_data_amount / total_count) * 100
        print(f"\rProgress: {progress:.2f}% ", end="")

    if export_type == "RDF/XML":
        with open(f"output_files/{filename}", "a") as f:
            f.write('</rdf:RDF>')
    print(f"\nRDF data exported to output_files/{filename}")





def parse_ontology(path: str = None) -> rdflib.Graph():
    # Instantiate a graph as defined in the rdflib library
    onto = rdflib.Graph()
    onto.parse(path, format='turtle')
    return onto


def cypher_loaders_from_onto(onto, mappings):
    """
    Use the written query to create cypher queries to obtain classes and its properties.
    """
    cypher_import = {}
    prop_names = []
    # onto.query returns two URIRef, the class name and its properties
    for row in onto.query(classes_and_props_query):
        # get class name
        URIRef = row[0].split('/')
        namespace = ''.join(URIRef[:-1])
        local = URIRef[-1]

        if local not in mappings:
            continue

        cypher = []
        try:
            cypher.append("unwind $records AS record")
            cypher.append(
                "merge (n:" + local + " { `" + \
                (mappings[local]["@uniqueId"] + \
                    "`: record.`" + \
                    mappings[local][mappings[local]["@uniqueId"]] + "`} )"
                    )
            )
        except Exception as e:
            print(f"Error in ontology.py {local}: {e}")

        # get properties
        for prop_and_type in row.props.split(","):
            # splits prop and type the prop is, then getting the prop name
            prop_name = prop_and_type.split(";")[0].split('/')[-1]

            #if a mapping (a column in the source file) is defined for the property and property is not a unique id
            try:
                query = "set n." + prop_name + " = record.`" + mappings[local][prop_name] + "`" if prop_name in mappings[local] else None
                if (prop_name in mappings[local] and prop_name != mappings[local]["@uniqueId"] and query not in cypher) :
                    cypher.append(query)
            except Exception as e:
                print("Error in ontology.py: ", prop_name, local)
            
        
        cypher.append("return count(*) as total")
        cypher_import[local] = ' \n'.join(cypher)
        # get relationships
        # row is a list of URIRef, the domain, relation, and range
    for row in onto.query(relations_query):
        #.rel and .dom is the variable in the relations query
        #relations and doma in
        rel = row.rel.split('/')[-1]
        dom = row.dom.split('/')[-1]

        # print('domain:', dom, dom in mappings,'relationship: ', rel, rel in mappings)
        # print('relationship: ', rel, rel in mappings)
        if dom not in mappings:
            continue
        if rel not in mappings:
            continue
        
        # range
        ran = row.ran.split('/')[-1]
        cypher = []

        cypher.append("unwind $records AS record")
        cypher.append("match (source:" + dom + " { `" + mappings[dom]["@uniqueId"] + "`: record.`" + mappings[rel]["@from"] + "`} )")
        cypher.append("match (target:" + ran + " { `" + mappings[ran]["@uniqueId"] + "`: record.`" + mappings[rel]["@to"] + "`} )")
        cypher.append("merge (source)-[r:`"+ rel+"`]->(target)")

        if rel:
            cypher.append("set r." + mappings[rel][rel] + "" + " = record.`" + mappings[rel][rel] + "`")

        cypher.append("return count(*) as total")
        cypher_import[rel] = ' \n'.join(cypher)


    return cypher_import

def sparql_loaders_from_onto(onto, mappings): # to import into graphDB
    pass


def export_rdf_from_src(onto, mappings, export_type="turtle"):
    """
    Create RDF graph of data from source files.

    - initiate the RDF graph
    - go through the ontology
    - read the mappings and corresponding CSV files
    - add the nodes and relationships to the RDF graph (we need to consider the order of the loading process)
    - serialize the graph
    """
    graph = rdflib.Graph()

    # Define prefixes
    sockg_prefix = "http://www.semanticweb.org/sockg/ontologies/2024/0/soil-carbon-ontology/"
    sockg_n4ind_prefix = "neo4j://graph.individuals#"

    graph.bind("sockg", sockg_prefix)
    graph.bind("sockg-n4ind", sockg_n4ind_prefix)

    entity_index = 0

    print("Creating Nodes...")
    for row in onto.query(classes_and_props_query):
        class_name = row[0].split('/')[-1]
        class_mappings = mappings.get(class_name)

        file_path = class_mappings['@fileName']
        if not os.path.isfile(file_path):
            continue

        df = pd.read_csv(file_path, low_memory=False)

        for df_index, row in df.iterrows():
            subject = rdflib.URIRef(f"{sockg_n4ind_prefix}{entity_index}")
            graph.add((subject, rdflib.RDF.type, rdflib.URIRef(f"{sockg_prefix}{class_name}")))

            entity_index += 1
            print(f"\rProgress: {(((df_index+1) / (len(df))) * 100):.2f}% {class_name}", end="") # +1 since index is zero-based

            for prop_name, prop_value in row.items():
                if pd.notna(prop_value) and prop_name in class_mappings and prop_name != class_mappings.get("@uniqueId"):
                    predicate = rdflib.URIRef(f"{sockg_prefix}{prop_name}")
                    if isinstance(prop_value, str) and prop_value.startswith("sockg-n4ind:"):
                        object_value = rdflib.URIRef(f"{sockg_n4ind_prefix}{prop_value.split(':')[-1]}")
                    else:
                        object_value = rdflib.Literal(prop_value)
                    graph.add((subject, predicate, object_value))
            

        print("") # for new line

    # Handle relationships
    print("\nCreating Relationships...")
    for row in onto.query(relations_query):
        rel_name = row.rel.split('/')[-1]
        dom_name = row.dom.split('/')[-1]
        ran_name = row.ran.split('/')[-1]

        rel_mappings = mappings.get(rel_name)

        dom_file_path = mappings.get(dom_name)['@fileName']
        ran_file_path = mappings.get(ran_name)['@fileName']

        if not os.path.isfile(dom_file_path) or not os.path.isfile(ran_file_path) or rel_mappings is None:
            continue

        dom_df = pd.read_csv(dom_file_path, low_memory=False)
        ran_df = pd.read_csv(ran_file_path, low_memory=False)

        ran_ids = set(ran_df[mappings[ran_name]['@uniqueId']].dropna().astype(str))

        if rel_mappings.get('@from') in dom_df.columns and rel_mappings.get('@to') in dom_df.columns:
            for index, row in dom_df.iterrows():
                from_value = row[rel_mappings['@from']]
                to_value = row[rel_mappings['@to']]

                if pd.notna(from_value) and pd.notna(to_value) and str(to_value) in ran_ids:
                    temp_ran_df = ran_df[ran_df[mappings[ran_name]['@uniqueId']] == to_value]
                    temp_dom_df = dom_df[dom_df[mappings[dom_name]['@uniqueId']] == from_value]
                    to_node_id = temp_ran_df.index[0] if temp_ran_df.shape[0] > 0 else None
                    from_node_id = temp_dom_df.index[0] if temp_dom_df.shape[0] > 0 else None

                    if to_node_id is None or from_node_id is None:
                        continue

                    from_subject = rdflib.URIRef(f"{sockg_n4ind_prefix}{from_node_id}")
                    predicate = rdflib.URIRef(f"{sockg_prefix}{rel_name}")
                    to_object = rdflib.URIRef(f"{sockg_n4ind_prefix}{to_node_id}")

                    graph.add((from_subject, predicate, to_object))

                print(f"\rProgress: {(((index + 1) / len(dom_df)) * 100):.2f}% {rel_name}", end="")
            print()
        elif rel_mappings.get('@from') in ran_df.columns and rel_mappings.get('@to') in ran_df.columns:
            for index, row in ran_df.iterrows():
                from_value = row[rel_mappings['@from']]
                to_value = row[rel_mappings['@to']]
                if pd.notna(from_value) and pd.notna(to_value) and str(to_value) in ran_ids:
                    temp_ran_df = ran_df[ran_df[mappings[ran_name]['@uniqueId']] == to_value]
                    temp_dom_df = dom_df[dom_df[mappings[dom_name]['@uniqueId']] == from_value]
                    to_node_id = temp_ran_df.index[0] if temp_ran_df.shape[0] > 0 else None
                    from_node_id = temp_dom_df.index[0] if temp_dom_df.shape[0] > 0 else None

                    if to_node_id is None or from_node_id is None:
                        continue

                    from_subject = rdflib.URIRef(f"{sockg_n4ind_prefix}{from_node_id}")
                    predicate = rdflib.URIRef(f"{sockg_prefix}{rel_name}")
                    to_object = rdflib.URIRef(f"{sockg_n4ind_prefix}{to_node_id}")

                    graph.add((from_subject, predicate, to_object))

                print(f"\rProgress: {(((index + 1) / len(ran_df)) * 100):.2f}% {rel_name}", end="")
            print()

    print("\nSerializing the graph...")
    with open(f"output_files/sockg_{date.today()}.{export_type}", "w") as f:
        f.write(graph.serialize(format=export_type))

    print("\nGraph serialized to output_files/graph.ttl")

if __name__ == '__main__':
    asyncio.run(rdf_query())
    # import_annotations_to_neo4j("mappings.csv", style_file_path="style.grass")