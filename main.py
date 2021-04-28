from flask import Flask, jsonify
from flask import request
from flask import render_template
import json
import csv
import requests
from elasticsearch import Elasticsearch

es = Elasticsearch()
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('/index.html')

@app.route("/shop/<type>/<offset>")
def shop(offset, type):
    return render_template('/shop_test.html')

@app.route("/product_details.html")
def details():
    return render_template('/product_details.html')

# def get_json():
#     with open("cap.dress.val.json") as json_file:
#         return json.load(json_file)

# def get_json():
#     with open("./cap.dress.val.json") as json_file:
#         return json_file.read()
# @app.route("/capDressVal")
# def get_json():
#     with open("./cap.dress.val.json") as json_file:
#         return json_file.read()


@app.route("/test")
def test():
    return render_template('test.html')

# @app.route("/getPhoto/<name>")
# def getPhoto(name):
#     with open('data.csv', 'r') as file:
#             reader = csv.reader(file)
#             for row in reader:
#                 if (row[0].split(" ; ")[0] == str(name)):
#                     print(str(row[0].split(" ; ")[1]))
#                     return(str(row[0].split(" ; ")[1]))

@app.route("/products/<type>/<offset>")
def getProductsOffset(offset,type):
    results = {"products":[]}
    off = int(offset)
    headers = {'Content-type': 'application/json'}
    for i in range((off-1)*10, off*10):
        r = requests.get("http://localhost:9200/"+ type +"/_doc/"+str(i), headers = headers)
        # print(r.text)
        results["products"].append(r.json())
    return results

@app.route("/refine/<currentIndex>/<filter>")
def refineSearch(currentIndex,filter):
    headers = {'Content-type': 'application/json'}
    taxList = []
    ids = []
    id1 = request.args.get('f1')
    id2 = request.args.get('f2')
    id3 = request.args.get('f3')
    ids.append(id1)
    ids.append(id2)
    ids.append(id3)


    
    for i in range(3):
        id = ids[i]
        req = requests.get('http://localhost:9200/'+currentIndex+'/_doc/'+id, headers = headers)
        js = json.loads(req.text)
        taxonomy = js["_source"]["taxonomy"]
        taxList.append(taxonomy)

    for t in taxList:
        print (t)
    return getProductsFilter(currentIndex, filter, "red", 0, 10000)



#example: filter/dresses/taxonomy/red/0/1000
@app.route("/filter/<currentIndex>/<filter>/<text>/<minPrice>/<maxPrice>")
def getProductsFilter(currentIndex, filter, text, minPrice, maxPrice):
    # text = request.args.get("text")
    # filter = request.args.get("filter")
    results = {"products": []}

    if (text == "empty"):
        body = {
            "query": {
                "range": 
                {
                            "price": {
                                "gte": str(minPrice),
                                "lte": str(maxPrice)
                            }
                }
            }
        }
    else:
        body = {
            "query": {
                "bool": {
                    "must": [
                    {
                        "range": {
                            "price": {
                                "gte": str(minPrice),
                                "lte": str(maxPrice)
                            }
                        }
                    },
                    {
                        "match": {
                            str(filter) : str(text)
                        }
                    }
                    ]
                }
            }
        }
    



    res = es.search(index= currentIndex, body=body)

    for i in res["hits"]["hits"]:
        results["products"].append(i)

    #print (len(results["products"]))

    return jsonify(results)







if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)