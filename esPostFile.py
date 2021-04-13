import requests
import json
import os

# files = ['file1.json', 'file2.json']
id = 0

for filename in os.listdir(os.getcwd()+"/products"):
    headers = {'Content-type': 'application/json'}
    req = requests.post('http://localhost:9200/test/_doc/'+str(id), data = open("./products/"+filename,'rb').read(), headers = headers)
    id+=1
    print (req.text)
    print (filename)