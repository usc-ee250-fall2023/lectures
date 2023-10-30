import requests
import sys
import json


## json style data
host = "13.64.52.196"  # Azure EE-250
if len(sys.argv) > 1:
    host = sys.argv[1]
myjson = {
    'name' : 'prof-red',
    'scores' : [56, 66, 56],
    'dp-the-best' : True
}
json_string = json.dumps(myjson)
r = requests.post('http://' + host + ':5000/submit', json=myjson)
print(f"Status Code: {r.status_code}, Response: {r.text}")
r = requests.get('http://' + host + ':5000/check?name=prof-red')
print(f"Status Code: {r.status_code}, Response: {r.text}")

# r = requests.post('http://localhost:5000/submit', 
#                   json={'name':'caleb', 'scores' : [56, 16, 56], 'dp-the-best' : True})
# print(f"Status Code: {r.status_code}, Response: {r.json()}")

# r = requests.post('http://localhost:5000/submit', 
#                   json={'name':'bronny', 'scores' : [56, 66, 56], 'dp-the-best' : False})
# print(f"Status Code: {r.status_code}, Response: {r.json()}")

#r = requests.get('http://' + host + ':5000/check?name=gprof2')
#print(f"Status Code: {r.status_code}, Response: {r.text}")
