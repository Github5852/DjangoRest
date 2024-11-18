import requests
import json

URL ='http://127.0.0.1:8000/studentapi/'

def get_data(id = None):
    data = {}
    if data is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL,data = json_data)
    data = r.json()
    print(data)
#get_data(2)

def post_data():
    data = {
        'name':'rupesh',
        'roll':150,
        'city':'thane'
    }

    json_data = json.dumps(data)
    r = requests.post(url = URL,data = json_data)
    data = r.json()
    print(data)

post_data()

def updated_data():
    data = {
        "id":5,
        'name':'Rohit',
        'city':'Latur'
    }

    json_data = json.dumps(data)
    r = requests.put(url = URL,data = json_data)
    data = r.json()
    print(data)

#updated_data()

def deleted_data():
    data = {
        "id":4,
    }

    json_data = json.dumps(data)
    r = requests.delete(url = URL,data = json_data)
    data = r.json()
    print(data)

#deleted_data()