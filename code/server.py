from neo4j import GraphDatabase, Session
from constants import create_mappings
from ontology import cypher_loaders_from_onto, parse_ontology, export_rdf_from_src, rdf_query
from data_preprocessing import create_directory, run_data_processing
from csv_editor import run_csv_editor
from utils import run_utils, delete_directory
from csv_merger import run_csv_merger
from give_unique_ID import run_give_unique_id
from datetime import datetime
import pandas as pd
import math
import time
import argparse
import os
import traceback
import rdflib
import asyncio
from neo4j.exceptions import ServiceUnavailable
import sys


def test_connection(session: Session):
    """
    Test connection to Neo4j database
    """
    query = """
    MATCH (n)
    RETURN n
    LIMIT 10
    """
    try:
        session.run(query)
    except Exception as e:
        print('Error connecting to Neo4j database: ', e)
        exit()


def insert_data(session: Session,
                query: str,
                dataframe: pd.DataFrame,
                mappings: str,
                current_batch=0,
                cypher_query: str = None,
                batch_size: int = 1024) -> dict:
    """
    Inserts data into Neo4j using batches.

    Args:
        session (neo4j.Session): The Neo4j session to execute the queries.
        query (str): The Cypher query to execute for inserting data.
        dataframe (pd.DataFrame): The DataFrame containing the data to be inserted.
        batch_size (int, optional): The size of each batch for insertion. Defaults to 500.

    Returns:
        dict: A dictionary containing the total inserted records, batch count, and elapsed time.
    """
    total_inserted_records = 0
    current_batch = current_batch // batch_size
    start_time = time.time()
    insert_batch = []
    skipped_records = 0

    print(f'Progress: {current_batch*batch_size}/{len(dataframe)}')
    while current_batch * batch_size < len(dataframe):
        current_batch_data = dataframe[
            current_batch*batch_size:(current_batch+1)*batch_size
        ].to_dict('records')

        try:
            if '@uniqueId' in mappings[cypher_query]:
                class_unique_id = mappings[cypher_query]['@uniqueId']
                valid_records = [
                    record for record in current_batch_data
                    if not (isinstance(record.get(class_unique_id), (int, float)) and math.isnan(record.get(class_unique_id)))
                ]
            else:
                start = mappings[cypher_query]['@from']
                end = mappings[cypher_query]['@to']
                valid_records = [
                    record for record in current_batch_data
                    if not (isinstance(record.get(start), (int, float)) and math.isnan(record.get(start))) and
                    not (isinstance(record.get(end), (int, float))
                         and math.isnan(record.get(end)))
                ]

            skipped_records += len(current_batch_data) - len(valid_records)
            insert_batch = valid_records
            print(f"size of insert batch: {sys.getsizeof(insert_batch)} bytes")
            result = session.execute_write(
                lambda tx: tx.run(query, parameters={
                                  'records': insert_batch}).data()
            )
            total_inserted_records += result[0]['total']

        except Exception as e:
            if 'SemanticError' in str(e):
                print(f"SemanticError: {e}")
            else:
                tb = traceback.format_exc()
                print(f"\n{tb}")
                exit()

        current_batch += 1
        if current_batch * batch_size <= len(dataframe):
            print(f'Progress: {current_batch*batch_size}/{len(dataframe)}')
        else:
            print(f'Progress: {len(dataframe)}/{len(dataframe)}')

    print(f"Skipped records: {skipped_records}")

    return {
        "total_inserted_records": total_inserted_records,
        "total_batches": current_batch,
        "elapsed_time": time.time() - start_time
    }


def profile_query(session, cypher_query):
    result = session.run(f"PROFILE {cypher_query}")
    for record in result:
        print(record)


def insert_function(cypher_query, specific_queries, total, mappings, cypher_queries:dict, session, batch_num=0):
    weird_queries = ['SoilChemicalSample', 'Harvest']
    empty_queries = []
    error_queries = []
    if cypher_query in specific_queries or len(specific_queries) == 0:
        try:
            df = pd.read_csv(
                "./"+mappings[cypher_query]["@fileName"], low_memory=False)
            # print(mappings[cypher_query]["@fileName"])
            print(cypher_queries[cypher_query])

            # idk why but on mac max memory threshold is reached on these two
            if cypher_query in weird_queries:
                result = insert_data(session, cypher_queries[cypher_query], df, mappings=mappings,
                                     batch_size=1024*3, current_batch=batch_num, cypher_query=cypher_query)
            else:
                result = insert_data(session, cypher_queries[cypher_query], df, mappings=mappings,
                                     batch_size=1024*8, current_batch=batch_num, cypher_query=cypher_query)
            total += result["total_inserted_records"]

            # Printing insertion result
            if result["total_inserted_records"] == 0:
                empty_queries.append(cypher_query)

            print(result)
        except Exception as e:
            error_queries.append(cypher_query)
            tb = traceback.format_exc()

            print(f"\n{tb}")

# significantly decreases time to insert data


def create_indexes(mappings: dict, query, session: Session, retries=3):
    class_index_query = "CREATE INDEX IF NOT EXISTS FOR (n:{query}) ON (n.{property})"
    relation_index_query = "CREATE INDEX IF NOT EXISTS FOR ()-[r:{query}]-() ON (r.{to_property}, r.{from_property})"

    if query in mappings:
        for key in mappings[query]:
            if key not in ['@fileName', '@from', '@to', '@uniqueId']:
                if '@uniqueId' in mappings[query]:
                    index_query = class_index_query.format(
                        query=query, property=mappings[query][key])
                else:
                    index_query = relation_index_query.format(query=query, to_property=mappings[query]['@to'],
                                                              from_property=mappings[query]['@from'])
                for attempt in range(retries):
                    try:
                        session.run(index_query)
                        break
                    except ServiceUnavailable as e:
                        if attempt < retries - 1:
                            print(f"ServiceUnavailable error: {e}. Retrying...")
                            time.sleep(2)  # Wait before retrying
                        else:
                            raise

        session.run("CALL db.awaitIndexes();")


def update_version_csv():
    current_time = datetime.now()
    formatted_time = current_time.strftime("%m/%d/%Y")
    with open('kg/version.csv', 'w') as f:
        f.write('versionDate\n')
        f.write(formatted_time)


def parse_arguments():
    parser = argparse.ArgumentParser(description="Data Processing")
    parser.add_argument('-a', '--all', nargs='?', const=True,
                        type=str, help="Process all excel files in the data folder")
    parser.add_argument('-f', '--files', nargs='+', type=str,
                        help="Specify multiple files to export to Neo4j")
    parser.add_argument('infile', nargs='?', type=str, default="AgCros.xlsx",
                        help="The file you want to export to Neo4j (default: data/Lincoln NECCIRR_040821 (1).xlsm")
    parser.add_argument('-d', '--debug', action='store_true',
                        help='Checks for missing data in the knowledge graph')
    return parser.parse_args()


def get_files_to_process(args):
    files_to_process = []
    if args.all is not None:
        directories = ["raw_data/Lincoln_data/", "raw_data/AgCROS_data/"]
        for directory in directories:
            for file in os.listdir(directory):
                if file.endswith((".xlsm", ".xlsx")):
                    files_to_process.append(os.path.join(directory, file))
    elif args.files:
        files_to_process = args.files
    else:
        files_to_process = [args.infile]
    return files_to_process


def validate_files(files_to_process):
    raw_directories = ["raw_data/Lincoln_data/", "raw_data/AgCROS_data/"]
    valid_files = []
    for file in files_to_process:
        for raw_directory in raw_directories:
            if file in os.listdir(raw_directory):
                valid_files.append(os.path.join(raw_directory, file))
                break
        else:
            raise FileNotFoundError(f"File '{file}' not found in data folder")
    return valid_files


def connect_to_neo4j():
    username = input("Username: ")
    password = input("Password: ")

    URI = "neo4j://localhost:7687"
    AUTH = (username, password)
    driver = GraphDatabase.driver(URI, auth=AUTH)
    session = driver.session(database="neo4j")
    test_connection(session)
    print("Connected to Neo4j")
    return session

def process_data(file):
    processed_data_path = create_directory(file)

    print("running data_processing...")
    run_data_processing(file, processed_data_path)

    print("running give_unique_ID...")
    run_give_unique_id(processed_data_path)

    print("running utils...")
    run_utils(processed_data_path)

    return processed_data_path


def main():
    update_version_csv()
    args = parse_arguments()

    if not args.debug:
        start_query = input(
            "Where do you want to start (Enter to start at the beginning): ")
        specific_queries = input("What queries do you want to run, separate by space (Enter to run all): ").split(
        ) if not start_query else []
        start_query = start_query or "Amendment"
        specific_queries = specific_queries if specific_queries != [''] else []

        files_to_process = get_files_to_process(args)
        valid_files = validate_files(files_to_process)

        # Process valid files (placeholder for actual processing logic)
        for file in valid_files:
            print(f"Processing file: {file}")


def neo4j_main():
    update_version_csv()
    args = parse_arguments()
    session = connect_to_neo4j()

    if not args.debug:
        start_query = input("Where do you want to start (Enter to start at the beginning): ")
        specific_queries = input("What queries do you want to run, separate by space (Enter to run all): ").split() if not start_query else []
        batch_num = int(input("How far in are you in the query (Enter to start at the beginning): ") or 0) if (start_query or specific_queries) else 0
        start_query = start_query or "Amendment"
        specific_queries = specific_queries if specific_queries != [''] else []

        files_to_process = get_files_to_process(args)
        valid_files = validate_files(files_to_process)

        try:
            for file in valid_files:
                processed_data_path = process_data(file)

                print("Importing CSV files into Neo4j...")

                onto = parse_ontology('kg/sockg_ontology_2024-11-15.ttl')
                mappings = create_mappings(processed_data_path)
                cypher_queries = cypher_loaders_from_onto(onto, mappings)
                sorted_queries = sorted(cypher_queries.keys())
                empty_queries = []
                error_queries = []
                total = 0

                if start_query in sorted_queries:
                    start_index = sorted_queries.index(start_query)
                else:
                    raise ValueError(
                        f"Query '{start_query}' not found in sorted_queries")

                for cypher_query in sorted_queries[start_index:]:
                    create_indexes(mappings, cypher_query, session)
                    if cypher_query == start_query:
                        insert_function(cypher_query, specific_queries, total, mappings, cypher_queries, session, batch_num)
                    else:
                        insert_function(cypher_query, specific_queries, total, mappings, cypher_queries, session)

                print('Empty queries:', empty_queries)
                print('Error queries:', error_queries)

                delete_directory(processed_data_path)
                print("Total inserted records:", total)

                session.close()

        except Exception as e:
            tb = traceback.format_exc()
            print(f"\n{tb}")
            delete_directory(processed_data_path)
    else:
        mappings = create_mappings("")
        properties_per_class = {}

        result = session.run("""CALL apoc.meta.nodeTypeProperties()
                                YIELD nodeType, propertyName
                                RETURN nodeType AS NodeType, 
                                count(propertyName) AS PropertyCount, 
                                collect(propertyName) AS PropertyKeys
                                ORDER BY NodeType;""")
        keys_per_type = {}
        for record in result:
            keys_per_type[record["NodeType"].replace("`", "").replace(":", "")] = (
                record["PropertyCount"], record["PropertyKeys"])

        for key in mappings.keys():
            if key[0].isupper():
                properties_per_class[key] = len(mappings[key].values()) - 2

        for key in sorted(properties_per_class.keys()):
            if key in keys_per_type:
                if properties_per_class[key] - keys_per_type[key][0] > 0:
                    print(f"{key} is missing {properties_per_class[key] - keys_per_type[key][0]} properties")
                    properties = set(list(mappings[key].keys())[2:])
                    kg_properties = set(keys_per_type[key][1])
                    print(f"Missing properties: {properties - kg_properties}\n\n")
            else:
                print(f"{key} is not loaded in the KG\n\n")


def rdf_main():
    args = parse_arguments()
    files_to_process = get_files_to_process(args)
    valid_files = validate_files(files_to_process)

    export_type = input("What format do you want to export to? (ttl, nt, rdf/xml, json-ld): ")
    try:
        for file in valid_files:
            processed_data_path = process_data(file)

            onto = parse_ontology('kg/sockg_ontology_2024-11-15.ttl')
            mappings = create_mappings(processed_data_path)

            print("Creating the rdf graph...")
            export_rdf_from_src(onto, mappings, export_type)

            print("Exported to output_files/rdf_data.ttl")
    except Exception as e:
        tb = traceback.format_exc()
        print(f"\n{tb}")
        # print(f"Error in rdf_main: {e}")


if __name__ == "__main__":
    while True:
        choice = input("Import into Neo4j or export RDF? (neo4j/rdf): ")
        if choice == 'neo4j':
            neo4j_main()
            break
        elif choice == 'rdf':
            rdf_main()
            break
        else:
            print("Invalid Choice.")
