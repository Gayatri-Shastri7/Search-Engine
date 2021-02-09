
import requests
import json
def get_raw_skills(description):
    url = "http://51.222.9.184:36540/enter index/_search"
    payload = "{\r\n    \"query\": {\r\n        \"bool\": {\r\n            \"must\": [\r\n                {\r\n                    \"match\": {\r\n     \"Keyword\": \" "+ description +" \" \r\n   }\r\n                }\r\n            ]\r\n        }\r\n    },\r\n    \"size\": 0,\r\n    \"aggs\": {\r\n        \"jobFunctions\": {\r\n            \"terms\": {\r\n                \"field\": \"Keyword.keyword\",\r\n                \"size\": 500\r\n            }\r\n        }\r\n    }\r\n}"
    HEADERS = {
        'Content-Type': "Enter here",
        'Authorization': "Enter here"
        }
    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=HEADERS)
    response_json = json.loads(response.text)
    buckets = response_json['aggregations']['jobFunctions']['buckets']
    existing_skills = []
    for bucket in buckets:
        if bucket['key'] not in existing_skills:
            existing_skills.append(bucket['key'])
    return existing_skills
# desc = input()
def show_skills(desc):

    existing_skills = get_raw_skills(desc)
    sorted_skills = sorted(existing_skills, key=len,reverse= True)
    # Give me the Bigger length skill only 
    final_skills = []
    for skill in sorted_skills:
        if skill in desc:
            #print (skill)
            desc = desc.replace(skill,'')
            final_skills.append(skill)
    return{"status":final_skills} 
