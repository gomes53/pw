import requests
import json

files = ['file1.json', 'file2.json']

for i in range(len(files)):
    headers = {'Content-type': 'application/json'}
    req = requests.post('http://localhost:9200/test/_doc/'+str(i), data = open(files[i],'rb').read(), headers = headers)
    print (req.text)
    print (i)