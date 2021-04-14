import requests
import json
import os
"""
# files = ['file1.json', 'file2.json']
id = 0

for filename in os.listdir(os.getcwd()+"/products"):
    headers = {'Content-type': 'application/json'}
    req = requests.post('http://localhost:9200/test/_doc/'+str(id), data = open("./products/"+filename,'rb').read(), headers = headers)
    id+=1
    print (req.text)
    print (filename)
"""
def putBytype():
    headers = {'Content-type': 'application/json'}
    file = open("./products/products_with_images_17k.json", 'rb').read()

    transformed = json.loads(file)

    for i in transformed:
        id = 0
        getI = str(i).replace("/","").replace(" ", "").replace("&","").replace("'","").replace(",","").lower()
        for j in transformed[i]:
            temp = json.dumps(j)
            req = requests.post('http://localhost:9200/'+getI+'/_doc/'+str(id), data = temp, headers = headers)
            print('http://localhost:9200/'+getI+'/_doc/'+str(id))
            id-=-1

def putAll():
    headers = {'Content-type': 'application/json'}
    file = open("./products/products_with_images_17k.json", 'rb').read()

    transformed = json.loads(file)
    id = 0

    for i in transformed:
        for j in transformed[i]:
            temp = json.dumps(j)
            req = requests.post('http://localhost:9200/all/_doc/' + str(id), data=temp, headers=headers)
            print('http://localhost:9200/all/_doc/' + str(id))
            id -= -1
putAll()