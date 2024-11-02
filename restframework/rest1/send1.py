import requests
import json
URL="http://127.0.0.1:8000/"
# url endpoint changes look at it
def update_data():
    data={
    'name':'nomos',
    'age':21
    }
    json_data=json.dumps(data)
    r=requests.put(url=URL,data=json_data)
    r1=r.json()
    print(r1)
# update_data()
def delete_data():
    data={
        'id':22
    }
    json_data=json.dumps(data)
    r=requests.delete(url=URL,data=json_data)
    r1=r.json()
    print(r1)
delete_data()
def get_data():
    data={
        'id':21
    }
    json_data=json.dumps(data)
    r=requests.get(url=URL,data=json_data)
    r1=r.json()
    print(r1)
# get_data()