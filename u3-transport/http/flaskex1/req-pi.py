import requests
import json

r = requests.post('http://192.168.0.246:5000/scores', data={'score':'70'})
if r.status_code == 200:
    myresponse = r.text
    print(myresponse)

r = requests.post('http://192.168.0.246:5000/scores', data={'score':'75'})
if r.status_code == 200:
    myresponse = r.text
    print(myresponse)

r = requests.get('http://192.168.0.246:5000/avg')
if r.status_code == 200:
    print("Get average returned: ", r.text)

r = requests.post('http://192.168.0.246:5000/scores', data={'score':'85'})
if r.status_code == 200:
    myresponse = r.text
    print(myresponse)

r = requests.get('http://192.168.0.246:5000/avg')
if r.status_code == 200:
    print("Get average returned: ", r.text)
    
r = requests.get('http://192.168.0.246:5000/lookup?index=1')
if r.status_code == 200:
    print("2nd score added ", r.text)
    
