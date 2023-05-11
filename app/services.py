import os
import json
from SPARQLWrapper import SPARQLWrapper, JSON


def query_sparql(endpoint_url, query):
    print("Running query")
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    res = sparql.query().convert()
    print("Done")
    return res


def get_data():
    endpoint_url = "https://query.wikidata.org/sparql"
    # Movies released after 2013 with imdb-id
    query = """
    SELECT DISTINCT ?item ?imdbId ?itemLabel ?directorLabel ?genreLabel ?pubdate
    WHERE {
      ?item wdt:P31 wd:Q11424.
      ?item wdt:P345 ?imdbId.
      ?item wdt:P57 ?director.
      ?item wdt:P136 ?genre.
      ?item wdt:P577 ?pubdate.
      FILTER((?pubdate >= "2013-12-31T00:00:00Z"^^xsd:dateTime))
      SERVICE wikibase:label { 
        bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". 
      }
    }
    """
    results = query_sparql(endpoint_url, query)
    results = results["results"]["bindings"]
    return results


def get_file_path():
    app_root = os.path.dirname(__file__)
    new_path = os.path.join(app_root, '../query.json')
    return new_path


def save_to_file():
    res = get_data()
    with open(get_file_path(), "w") as outfile:
        json.dump(res, outfile)


def read_data_from_file():
    with open(get_file_path()) as f:
        data = json.load(f)
    return data


# if __name__ == "__main__":
#     save_to_file()
#     print(len(get_data_from_file()))
