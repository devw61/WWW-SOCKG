<img src="sockg_logo.jpg" alt="sockg logo" width="300px">

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Neo4j Setup](#neo4j-setup)
  - [Download Neo4j DB](#download-neo4j-db)
  - [Install Neo4j](#install-neo4j)
  - [Run Neo4j](#run-neo4j)
  - [Visualize KG Data in Neo4j](#visualize-kg-data-in-neo4j)
  - [Access SOCKG-Neo4j](#access-sockg-neo4j)
- [Data Loading for Neo4j](#data-loading-for-neo4j)
  - [Local environment and KG setup](#local-environment-and-kg-setup)
- [Workflow Documentation](#workflow-documentation)
  - [1. Running Data Processing](#1-running-data-processing)
  - [2. Running Utils](#2-running-utils)
  - [3. Running ontology \& constants](#3-running-ontology--constants)
  - [4. Running Server](#4-running-server)
- [Creating the Ontology](#creating-the-ontology)
  - [Background](#background)
  - [Download Protégé](#download-protégé)
  - [Becoming Familiar With Protégé](#becoming-familiar-with-protégé)
  - [Creating Classes](#creating-classes)
  - [Creating Properties](#creating-properties)
  - [Creating the Ontology from the Data Files](#creating-the-ontology-from-the-data-files)
  - [Identifying the Classes](#identifying-the-classes)
  - [Identifying the Data Properties](#identifying-the-data-properties)
  - [Identifying the Object Properties](#identifying-the-object-properties)


## Overview

The purpose of this knowledge graph (KG) is to investigating the factors influencing Soil Organic Carbon (SOC), and other key measurements, aim of reducing atmospheric carbon. This contributes to mitigating climate change while enhancing farm productivity.

In this project, we are using the GRACENet database from the United States Department of Agriculture (XXXX). The ontology is defined using [Protégé ](https://protege.stanford.edu/) and the soil carbon data is imported into [Neo4j](https://neo4j.com/).

Specifically, our project involves three key aspects:
1. Expert Consultation: We collaborated with XXXX experts to better understand the soil carbon data and to define the ontology, specifying the classes and properties.
2. Data Loading with Neo4j: We automated the creation of nodes (entities) and their relationships, allowing us to structure the data into an accessible knowledge graph.
3. Testing Hypotheses: By analyzing the relationships within GRACENet, we can form hypotheses and test them by generating graphs that reveal correlations between various measurements, including changes over time.

We aim to uncover insights and solutions that address unanswered questions in soil carbon research.

## Neo4j Setup

### Download Neo4j DB
Download Neo4j Graph Database from its official website: https://neo4j.com/deployment-center/

### Install Neo4j
We installed Neo4j Community Edition 5.15 on Linux, check the official doc if you use other versions or OS
``` py
tar -zxvf {downloaded neo4j tar file}
```

Make sure you have correct version of JDK. Neo4j 5.15 uses JDK 17

### Run Neo4j
``` py
[neo4j-root-folder]$ ./bin/neo4j start
```

### Visualize KG Data in Neo4j
Open your browser and go to: http://localhost:7474

The default account and password are both "neo4j"

You can use a **.grass** file to style the appearance of nodes and edges, similar to how CSS is used on the web. For instance, the **.grass** file allows you to customize node appearances such as color, size, and captions, which is especially helpful when visualizing graphs with multiple classes of nodes. In our root directory, we provide a **sockg_style.grass** file, which configures the colors and captions for each node class, making the visualization cleaner and easier to read in the Neo4j Browser.

### Access SOCKG-Neo4j
Our SOCKG Neo4j is publicly available at: https://XXXX.XXXX.edu/sockg-neo4j

One can access it through a BOLT connection and using the designated account and password.

A detailed tutorial can be found here: https://vimeo.com/929653567

## Data Loading for Neo4j

### Local environment and KG setup

There are a few requirements to this process:

* You must download the packages in `requirements.txt` using `pip install -r requirement.txt`
* The file you are importing must be an Excel sheet (`.xlsm` or `.xlsx`)
* The Excel file must be in the current (2024) DET Format
* `cd` to the `sockg/` directory, if not, then everything will not run

\todo{Do we need to mention the user should ensure the neo4j server is running either locally or on the server? In addition, the port number should be correct.}

Now that you have met these requirements all you have to do is run:

``` py
sudo python ./src/server.py <file_name>
```

Or to load all the files under `raw_data` folder:

``` py
sudo python ./src/server.py -a
```

Or to load multiple files:

``` py
sudo python ./src/server.py -f <file_name> <file_name2>...
```


## Workflow Documentation
### 1. Running Data Processing

Within the `src/data_processing.py`, multiple actions are performed. First, the program reads the Excel file and convert each sheet into a CSV file for later use.

``` py linenums='1' hl_lines='3 4 5 6 7 8 9 10'
    def run_data_processing(excel_path: str,directory_path: str):
        ### Step 1: read xlsx file and seperate them into raw files
        excel_file = pd.ExcelFile(excel_path)

        # Iterate through each sheet and save as CSV
        for sheet_name in excel_file.sheet_names:
            df = pd.DataFrame()

            if excel_path.split("/")[-1] == "AgCros.xlsx":
                df = pd.read_excel(excel_file, sheet_name=sheet_name)
```

Next, all empty values must be replaced with NaN, Not a Number, to differentiate between the string ‘None’ and having an empty value.

``` py
df = df.replace(" ", pd.NA)
```

To make the data more understandable, we need to rename the columns, as these names will later represent data properties in the KG. We created a function in `constants.py` called `property2columnGRACENET()`, which is a dictionary between the original terms and readable new terms. Additionally, the column names from the data base are in snake case (this_is_snake_case) and our data properties are in camel case (thisIsCamelCase) so we created a simple script which converts any columns we did not specify in `property2columnGRACENET()` to be in the same fromat as our KG data properties.

To use our dictionary we call a function in `utils.py` called `apply_column_mapping()` which takes the parameters of a dataframe, the current sheet name, and whether or not this is a gracenet file to consider both the 2020 and 2024 DET formats.

``` py title='data_processing.py'
df = apply_column_mapping(df,sheet_name)
```

`apply_column_mapping()` will iterate through the columns of the old data frame, calling `column2property()`, or `property2columnGRACENET()` depending on the value of `gracenet`, in `src/constants.py` each time to check if the string input into the function is there. If the string is indeed within the dictionary, it must be replaced, changing the column name to its key-value pair.

```py title='utils.py'
for column in input_df.columns:
    if gracenet == False and column2property(column,sheet_name)!=None:
        # rename column
        input_df.rename(columns={column: column2property(column, sheet_name)}, inplace=True)
```

``` py title='example of dictionary in column2property()'
elif sheet_name == "Citations":
    mapping = {
        "Site ID": "siteId",
        "Date Published": "publicationDate",
        "Type": "publicationType",
        "Title": "publicationTitle",
        "Is Part Of": "bookName",
        "Author": "publicationAuthor",
        "Correspond Author": "publicationCorrespondingAuthor",
        "Identifier": "publicationIdentifier",
        "Description": "publicationDescription",
        "Citation": "publicationCitation",
    }
```

The next part of code is simple as it renames csv files and removes any files that do not pertain to our research.

### 2. Running Utils

Utils holds a small but important task of correctly adding columns from one CSV file to another. Sometimes the files we access to create a class do not hold all the information we want it to. By
converting the two CSV files into data frames, we can merge them based on a specific column we want added, and then replace the output CSV file with the updated one.

In detail, we call the function `move_column()` that takes the parameters of the input and output CSV files, the column to compare the two data frames, and the column we want to add to the output CSV file.

``` py
def move_column(input_csv, output_csv, column_to_move: str, compared_column_input_df, compared_column_output_df: str):
    try:
        output_df = pd.read_csv(output_csv, low_memory=False)
        input_df = pd.read_csv(input_csv, low_memory=False)


        merged_df = output_df.merge(input_df[[compared_column_input_df, column_to_move]],
                                    left_on=compared_column_output_df,
                                    right_on=compared_column_input_df,
                                    how='left',
                                    suffixes=('', ''))

        merged_df = merged_df.drop_duplicates()
        merged_df.to_csv(output_csv, index=False)
```

In this function, we read both the input and output CSV files which converts them into dataframes we can manipulate. From this, we use the `.merge()` function in pandas that compares the two columns specified as `compared_column_output_df` and `compared_column_input_df` and adds `column_to_move` if the two values on that row for those two columns are the same. However, nothing is perfect and some rows are duplicated so we must drop those to create a clean data frame for us to use in later stages of research. Finally, we simply export the merged dataframe with the same name as the output dataframe which just updates the file.

### 3. Running ontology & constants

Before we reach the final step of running server.py I will talk about an important part of server.py that accesses a different file, `ontology.py`. There are 3 main functions that are called in server.py. They are `parse_ontology()`, `create_mappings()`, and `cypher_loaders_from_onto()` each with their own individual purposes buildings off another.

We first call `parse_onotology()` taking the parameter of the .ttl file location and returns a rdflib Graph. This accomplishes multiple goals. First, is creating a standardized format for the data we can take advantage of later. Next, we can easily access the graph to manipulate or verify the data within. Additionally, it has robust query capabilities which we utilize heavily later on.

Next, we call `create_mappings()`. Taking the parameter of the processed_data path, according to the specific file being imported. Creating mappings sets up the structures of both the classes and relationships. We later call this to check if the strings within the files we access to import the data have the same column names as they are supposed to. How the class structure is set up with three main components: file path, unique ID, and data properties.

``` py title='exmaple of a class structure'
experiment_struct = {
    '@fileName': raw_path + r'/overview.csv',
    '@uniqueId': 'experimentName',
    'experimentName': 'experimentName',
    'experimentStartDate': 'experimentStartDate',
    'experimentEndDate': 'experimentEndDate',  # ExperUnits
    'durationOfStudy': 'durationOfStudy',
    'projectName': 'projectName',
}
mappings['Experiment'] = experiment_struct
```

The relations structure, similar to the class structure, holds 3 main components: the file path, the starting, and ending points of the relation. The fourth line is just to show semantically, in this case, 'projectName' funds the experiment. Now you might be asking how neo4j knows what class to point to. This is specified in the ontology with the starting class represented as the 'domain' and the ending class represented as the 'range'.

``` py title='example of a relationship structure'
fundsExperiment_struct = {
    '@fileName': raw_path + r'/overview.csv',
    '@from': 'organizationName',
    '@to': 'projectName',
    'fundsExperiment': 'projectName',
}
mappings['fundsExperiment'] = fundsExperiment_struct
```

``` title='example of a relation in the ontology'
###  http://www.semanticweb.org/sockg/ontologies/2024/0/soil-carbon-ontology/appliedInExpUnit
:appliedInExpUnit rdf:type owl:ObjectProperty ;
                  rdfs:domain :Treatment ;
                  rdfs:range :ExperimentalUnit .
```

The final function called is `cypher_loaders_from_onto()` taking the parameters of our parsed ontology and the mappings dictionary we just created. Looking at the function in detail, the first for loop automatically creates the cypher queries for classes and their data properties. Querying the graph returned by `parse_ontology()` with a query called `classes_and_props_query` (created in `constants.py`) returning all of the classes along with their data properties. This is our form of data validation to make certain data properties are meant to be there.

```py
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
        cypher.append("unwind $records AS record")
        cypher.append("merge (n:" + local + " { `" + (mappings[local]["@uniqueId"] + "`: record.`" + mappings[local][mappings[local]
                        ["@uniqueId"]] + "`} )")
        )
```

Notice cypher_import is an empty dictionary and prop_names is an empty list, these will be used later.

Next begins our verification of data.

``` py
# get properties
for prop_and_type in row.props.split(","):
    # splits prop and type the prop is, then getting the prop name
    prop_name = prop_and_type.split(";")[0].split('/')[-1]

    #if a mapping (a column in the source file) is defined for the property and property is not a unique id
    if (prop_name in mappings[local] and prop_name != mappings[local]["@uniqueId"]):
        prop_names.append(prop_name)
        cypher.append("set n." + prop_name + " = record.`" + mappings[local][prop_name] + "`")
```

Let's first explain the for loop. Obviously you have your variable that represents the iteration of `row.props.split(",")` but you probably do not know what `row.props.split(",")` means. The variable row is just the row of data we are analyzing but `.props` is a little more complicated. From the sparql query we just ran, `classes_and_props_query`, two values were returned: `?class` and `?props`. `.props` specifically accesses the variable `?props`. It's similar to when you're accessing functions in packages like `pd.DataFrame`. Finally, `.split(",")` is a function that is often used which split the string based on the specific string or, in this case, character.

Moving on, we now need to acquire the property name which we do so by this line:

``` py
prop_name = prop_and_type.split(";")[0].split('/')[-1]
```

The `if` statement is simple when you understand it. All it is doing is checking if the property name is in the dictionary under the specific class and isn't the unique ID of the class since it is already inserted by neo4j. From this, we append the unique cypher query for that prop name to a list of accepted cypher queries.

The same process is used to check the relations. Using a for loop accessing the `.rel` variable returned by the `relations_query` and checking if both the domain and relationship are in the mappings dictionary. Appending the appropriate SPARQL query to the local list of cypher queries

Eventually, the resulting lists of for loops are appended to a unifying list of cypher queries that has both the queries for classes and relations. Now we are ready to run `server.py`

### 4. Running Server

Finally, we reach the culmination of everything. `server.py` accomplishes two goals: the automation of importing into the KG and importing the data.

Often times the developer will not want to import the whole data set so we created a few scenarios which significantly reduce run time. First are the command line arguments we stated earlier in 'How to import into the KG'. The second is the option to start at a certain query or to only run specific queries. Since the order of queries is constant, if the user could not finish importing into their KG they could pick up where they left off. Additionally, if the user wants to update certain classes within the KG they can just run those queries without running every query.

The main section of the code is relatively simple. All that is accomplished is calling the run functions from each file needed for pre-processing.

``` py title='example of calling a run function'
from give_unique_ID import run_give_unique_id
...
# give_unique_ID
print("running give_unique_ID...")
run_give_unique_id(processed_data_path)
```

Next, we connect to the KG with the built-in functions `GraphDatabase.driver()` and `.session()` using the appropriate credentials to log into the server. Sometimes, however, we will fail to establish a connection with neo4j so we test the connection with a simple cypher query. This will give us an error and will help us identify if the error that occurs is truly just a connection error or an error with our code.

``` py
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
```

Diving into the for loop, this begins the insertion of data into the KG by iterating through the sorted_queries list. While the loop looks like it is only set up for starting in the middle of the query, earlier the start_query was set to the first query, and batch_num was initialized as zero so we are just explicitly telling the loop to start at the beginning instead of implicitly doing so. Two things are accomplished, indexing the query and its data properties and inserting the data. In each iteration of the for loop, we call the function `created_indexes()` and `insert_function()`. `created_indexes()` is a major component of inserting data as it decreases our run time by a factor of at least 10. Without getting into detail on what its queries do, imagine rather than blindly finding where the node is within the memory we are giving the program a golden road that leads straight to the node.

``` py
if start_query in sorted_queries:
    start_index = sorted_queries.index(start_query)
else:
    raise ValueError(f"Query '{start_query}' not found in sorted_queries")

for cypher_query in sorted_queries[start_index:]:
    create_indexes(mappings, cypher_query, session)
    if cypher_query == start_query:
        insert_function(cypher_query,specific_queries, total, batch_num)
    else:
        insert_function(cypher_query,specific_queries, total)
```

`insert_function()` takes the parameters of the current cypher_query iteration, the list of specific_queries, the total number of nodes that have been inserted, and the optional batch_num that is automatically set to 0 if the parameter is not passed. Within this function, 3 main actions occur. Creating the dataframe that will be passed into the `insert_data()` function, optimizes the batch size based on which query is being inserted, and updates the total number of nodes inserted.

``` py
result = insert_data(session, cypher_queries[cypher_query], df, mappings=mappings,
                    batch_size=1024*3, current_batch=batch_num)
```

`insert_data()` takes the parameters of the neo4j session, the actual cypher query rather than the name of the cypher query, the dataframe that was just created, the mappings dictionary, the batch size for that query, and a variable that tells the function where to start inserting data within the dataframe. Looking at the details of `insert_data()` we utilize a while loop that continuously runs until we have reached the end of the dataframe. Within each iteration of the while loop, we initialize the batch of data we are inserting, filtering out rows of data which have NaN values for their UIDs or for their start or end destinations. The reason for this is each node is inserted based on its UID, specified in the mappings dictionary under the key corresponding to the cypher query name, and cannot have the value of NaN otherwise an error will be thrown and the rest of the data will not be inserted.

``` py
record for record in current_batch_data
if not (isinstance(record.get(class_unique_id), (int, float)) and math.isnan(record.get(class_unique_id)))
```

``` py
if not (isinstance(record.get(start), (int, float)) and math.isnan(record.get(start))) and
not (isinstance(record.get(end), (int, float))
    and math.isnan(record.get(end)))
```

Then we insert the filtered list of nodes that can be inserted by using the built-in function `.execute_write()` and using a lambda function which tells the `.execute_write()` function the query and to look at the filtered list of data.

```py
result = session.execute_write(
    lambda tx: tx.run(query, parameters={'records': insert_batch}).data()
)
```

This ends our program and returns any queries that were empty or an error was thrown while inserting the data for that class. Allowing the user to realize any bugs that might arise however expect at least a couple of queries to be empty as there is usually no data in some tabs. Additionally, we delete the directory which holds the processed data as this process takes very little time while holding massive amounts of data at the same time making it the effort to hold the data not worth it so we delete it and create it again next time the program is ran.

## Creating the Ontology

### Background

An ontology is a structured framework that organizes information by defining the relationships between concepts within a particular domain. For the purposes of our project, the ontology details the structure of the knowledge graph, thus serving as a blueprint for the knowledge graph.

An ontology includes a set of entities, with the most prominent ones being Classes, Data properties, and Object properties.

Classes describe concepts in the domain. Some examples of classes would include "Person" and "Organization".

Data properties describe the attributes of the classes. For example, the classes "Person" and "Organization" would both have the data property "name", as both people and organizations have names. The "Person" class can also have other data properties such as "age", "weight", "height", "email", etc. Similarly, the "Organization" class might have data properties such as "profits", "headquarters", and "employeeCount".

Data properties have a domain and range. The domain of a data property is the class that it belongs to. For example, in the previous example the data property "height" would have domain "Person" because it is a data property of the "Person" class. The range of a data property is the data type of the values represented by the data property. The most common values for the range of a data property are: xsd:int for integers, xsd:float for decimals, xsd:string for text, and xsd:dateTime for dates, although there are many more options. The range for data properties "weight" and "height" would most likely be xsd:float (this depends on the dataset), the range for data property "age" would be xsd:int, and the range for "email" would be xsd:string.

Object properties describe relationships between classes. For example, people and organizations are related because people work for organizations. Therefore, we can create an object property called "worksFor" that tells us that the class "Person" "worksFor" the class "Organization". This relationship is directional (meaning "Person" "worksFor" "Organization" is true but "Organization" "worksFor" "Person" is not true), and the direction is determined by the domain and range of the object property.

Think of the relationship described by an object property as a class pointing with an arrow to another class. In our example, the "Person" class points to the "Organization" class. The domain is the class that is doing the pointing (in this case the "Person" class) and the range is the class that is being pointed at (the "Organization" class in this case). More formally, the domain is the subject of the relationship and the range is the object of the relationship. After becoming familiar with these entities, we are now ready to create the ontology.

### Download Protégé

Our ontology was created using Protégé, which can be downloaded from its official website: [https://protege.stanford.edu/](https://protege.stanford.edu/)

### Becoming Familiar With Protégé

Opening Protégé will present you with a default empty ontology. At this point, you can load an ontology such as our `soil_carbon_ontology.ttl` that can be found under the `kg/` directory or you can create an ontology from scratch.

The Ontology IRI field allows you to provide an IRI that will be used to identify the ontology over the web.

The Entities tab is where you will spend most of your time while using Protégé. From here, you can create and modify Classes, Data properties, and Object properties from their respective tabs. Each of these have a root entity that cannot be deleted in Protégé. These are owl:Thing, owl:topDataProperty, and owl:topObjectProperty for Classes, Data properties, and Object properties, respectively.

### Creating Classes
To create a new class: 
1. Click on the owl:Thing root class and click the "add subclass" button. 
2. Enter the name of the class and confirm at the prompt.

### Creating Properties

To create a new data or object property:
1. Navigate to the corresponding tab and click on the root property (owl:topDataProperty or owl:topObjectProperty).
2. Click the "add sub property" button, enter the name of the property, and confirm at the prompt. 
3. Click on the "+" icon next to the "Domains (intersection)" label and select the appropriate domains for the property. 
4. Click on the "+" icon next to the "Ranges" label and select the appropriate ranges for the property. 

### Creating the Ontology from the Data Files

We will illustrate an example of creating an ontology from a sample of data. For this example, we will use a small sample of the data found in the "WeatherDaily" sheet of `"Lincoln NECCIRR.xlsm"`, which can be found under the `raw_data/Lincoln_data` directory.

| Site ID | Field ID | Weather Date | Weather Station ID | Temp Max degC | Temp Min degC | Precip mm/d | Bad Value Flag | RH % | Dew Point degC | Wind Speed m/s | Solar Radiation Veg MJ/m2/d | Solar Radiation Bare MJ/m2/d | Soil Temp 5cm degC | Soil Temp 10cm degC | Wind Direction deg from N | Open Pan Evap mm/d | Closed Pan Evap mm/d | Atmos N Deposition kg/ha/d | Total Net Radiation MJ/m2/d | Snow mm/d |
|---------|----------|---------------|-------------------|----------------|---------------|---------------|----------------|--------|----------------|------------------|-------------------------------|-------------------------------|--------------------|---------------------|-------------------|---------------------|----------------------|-------------------------------|-------------------------------|------------|
| NECCIRR | NECCIRR  | 5/19/2010     | HARVARD 4SW        | 14.37          | 11.02         | 11.43         |                | 91.258 |                | 3.91517632       | 3.192518736                   | 14.78055556                   | 0.914              |                     |                   |                     |                      |                               |                               |            |
| NECCIRR | NECCIRR  | 5/20/2010     | HARVARD 4SW        | 14.42          | 10.63         | 22.606        |                | 96.867 |                | 3.87941312       | 4.50227538                    | 13.89333333                   | 0.711              |                     |                   |                     |                      |                               |                               |            |
| NECCIRR | NECCIRR  | 5/21/2010     | HARVARD 4SW        | 22.8           | 10.07         | 0             |                | 79.481 |                | 3.095752         | 23.56385468                   | 17.27722222                   | 5.232              |                     |                   |                     |                      |                               |                               |            |

### Identifying the Classes

The first step is to identify the broader concepts that are being described by the data, which will then be added to the ontology as classes. A quick glance at the column names and sample data will reveal a variety of concepts. The concepts represented in this sample data are: "Site", "Field", "WeatherObservation", and "WeatherStation". After identifying these concepts, we simply add them as classes in our ontology using Protégé.

### Identifying the Data Properties

The next step is to create the data properties for the classes we just created. This can be accomplished simply by analyzing the column names. For example, the columns "Site ID", "Field ID", and "Weather Station ID" tell us that the classes "Site", "Field", and "WeatherStation" have "ID" data properties. Furthermore, using our intuition, we can determine that the rest of the columns are properties of "WeatherObservation" (it's trivial that values such as temperature, humidity, and precipitation are properties of the weather). 

Once we identify the data properties, we create them in the ontology and add their respective domains. In our example, the domain of data property "siteId" is "Site", the domain of "fieldId" is "Field", the domain of "weatherStationId" is "WeatherStation", and the domain of all the weather data properties is "WeatherObservation". 

Now we look at the values of the data properties (the values in the rows of the data file) to determine the ranges of the data properties. We can see that the "ID" data properties contain text such as "NECCIRR" and "HARVARD 4SW	", so the range for these data properties would be xsd:string. We can see that some of the data properties have decimal values, so the range of these would be xsd:float. Some of the other data properties don't have any values in this data file, but we can make educated guesses regarding their range. Since all of the numerical values we have looked at so far have been of type xsd:float, we can reasonably assume that the same will be true for all the other numerical data in this sample of data. 

The "Bad Value Flag" column is noteworthy here because it doesn't have any values and doesn't appear to be a numerical value, so we can't just assume that its range will be xsd:float. This highlights the importance of being familiar with the dataset when modeling it with an ontology. In the original excel file, clicking on the "Bad Value Flag" cell will reveal a note that reads: "If weather data for a particular day are missing or suspect, enter -999, else leave blank". With this newfound knowledge, we can determine that the range for the "weatherBadValueFlag" data property should be xsd:int.

### Identifying the Object Properties

Finally, we will analyze our sample data for relationships between classes and model these with object properties. Object properties are the most difficult to model because they require in-depth understanding of the dataset. During the creation of our ontology, there were many times when we had to consult our XXXX collaborators to ask for clarification and guidance to ensure we accurately modeled the data.

Since this sample data is describing the weather, a topic most are familiar with, we can find relationships using our intuition. The clearest relationship is the one between "WeatherStation" and "WeatherObservation" because its trivial that weather stations are the ones recording the weather. Therefore, we can create an object property named "recordsWeather" that would indicate that "WeatherStation" "recordsWeather" "WeatherObservation" (the weather station records a weather observation). Since "WeatherStation" is the subject of the relationship, it should be the domain of the object property. "WeatherObservation" is the object of the relationship, so it should be the range of the object property.

Clicking on the "Field ID" cell in the original excel file will reveal a note that reads: "FieldID that weather data is associated with", directly informing us that the classes "Field" and "WeatherObservation" have a relationship. As a result, we can create an object property called "hasWeather" that tells us that "Field" "hasWeather" "WeatherObservation". The domain of this object property would be "Field" and the range would be "WeatherObservation".

These are the only object properties that are clearly defined in this sheet of the excel file, but it's crucial to keep looking for relationships among classes in the other data sheets even if the classes weren't originally created in said sheets. For example, even though the classes "Site" and "WeatherStation" were created in the "WeatherDaily" sheet in our example, the "WeatherStation" sheet reveals that these classes are related, so we would need to create an object property for this relationship even though it wasn't obvious in the "WeatherDaily" sheet.

Repeat this process for as many data files as you would like and you eventually end up with an ontology that is ready to be loaded into a knowledge graph.
