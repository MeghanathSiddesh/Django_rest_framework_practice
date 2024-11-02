import requests
import json
URL='http://127.0.0.1:8000/'
data={
    'id':1,
    'name':'Megha',
    'roll':65
}
json_data=json.dumps(data)
response=requests.put(url=URL,data=json_data)
r=response.json()
print(r)