import requests
import json

URL = 'http://127.0.0.1:8000/stucreate/'

data = {
    'name':'sachin',
    'roll':101,
    'city':'nsk'
}

json_data = json.dumps(data)

r = requests.post(data = json_data,url=URL)
print(r)
data = r.json()
print(data)