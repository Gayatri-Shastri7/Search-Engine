import csv 
from elasticsearch import Elasticsearch 

#by default we connect to localhost:9200
es = Elasticsearch() 

#create index in elasticsearch , ignore satus code 400(index alreay exists)
es.indices.create(index="skills_taxonomy",ignore=400)

with open("categories.csv") as f:
    reader = csv.DictReader(f)
    for line in reader:
        es.index(index="skills_taxonomy", doc_type="skills", body=line)