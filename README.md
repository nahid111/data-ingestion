# A data ingestion mini project
<hr/>

## Task
1. Firstly, to recover some raw data from https://query.wikidata.org/ This data should be movies that had been released after 2013 and have imdb-id.
2. Then the data should be ingested in a database by using a conception of entity-relation (which must respect some normalizations).
3. Finally, display some tables of the data stored in the database in a simple interface.

## Getting Started 
1. clone the repo & cd into it.
2. Create a virtual environment for installing dependencies: 
<br/><nbsp/>`$ python3 -m venv project_name_venv`
3. Source the virtual environment:
<br/><nbsp/>`$ source project_name_venv/bin/activate`
4. Install the dependencies in the virtual environment: 
<br/><nbsp/>`$ pip install -r requirements.txt`

## Running it
1. set env: 
<br/><nbsp/>`$ export FLASK_APP=app`
2. Create an admin user
<br/><nbsp/>`$ flask fab create-admin`
3. Run dev server
<br/><nbsp/>`$ flask run`

