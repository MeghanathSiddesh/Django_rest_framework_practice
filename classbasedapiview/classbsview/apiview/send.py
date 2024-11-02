import requests
import json
URL='http://127.0.0.1:8000/'
headers={'content-type':'application/json'}
def get():
    data={
        'id':2
    }
    json_data=json.dumps(data)
# while sendin gsome data from this app we need to specify the media type we are sending
    res=requests.get(url=URL,headers=headers,data=json_data)
    r1=res.json()
    print(r1)
# get()
def post():
    data={
        'name':'Meghanath',
        'age':21,
        'roll':65,
        'city':'Banglore'
    }
# here we need to specify the media type while sending the data to apiview i.e.. application/json
    json_data=json.dumps(data)
    res=requests.post(url=URL,headers=headers,data=json_data)
    r=res.json()
    print(r)
post()
def update():
    data={
        'id':4,
        'name':'Rohan'
    }
    json_data=json.dumps(data)
    resp=requests.put(url=URL,headers=headers,data=json_data)
    r=resp.json()
    print(r)
# update()
def delete():
    data={
        'id':4,
    }
    json_data=json.dumps(data)
    resp=requests.delete(url=URL,headers=headers,data=json_data)
    r=resp.json()
    print(r)
# delete()