import csv 
import json
import requests
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import uuid

extract_url = 'http://localhost:9200/skills_taxonomy'
copy_url = 'http://51.222.9.184:36540/'


def load_csv():
    filename="Categories.csv"
    data = [row for row in csv.reader(open(filename, 'r'))]
    data = data[1:]   
    print(len(data))     
    return(data)

def copy_to_new_elastic(temp):
    print("copying to new elastic index started")
    HEADERS = {
        'content-type':'Enter here',
        'Authorization': 'Enter here'
        }
    es = Elasticsearch(hosts=[copy_url], timeout=5000, headers=HEADERS)
    data = []
    for i in range(len(temp)):
        _temp = {}
        _temp['_index'] = 'skills_taxonomy'
        _temp['_type'] = 'skills'
        _temp['id'] = str(uuid.uuid4())
        _temp['_source'] = {}
        _temp['_source']['keyword'] = temp[i][0]
        _temp['_source']['keyword_type'] = temp[i][1]
        
        data.append(_temp)
        print(i)
    try:
        success, _ = bulk (es, data)
    except Exception as error:
        print(error)
    print('finished')
                
if __name__ == '__main__':
    temp= load_csv()
    copy_to_new_elastic(temp)
