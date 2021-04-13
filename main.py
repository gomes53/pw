from flask import Flask
from flask import request
from flask import render_template
import json
import csv
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('/index.html')

@app.route("/shop")
def shop():
    return render_template('/shop.html')

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

@app.route("/products/<offset>")
def getProductsOffset(offset):
    results = {"products":[]}
    off = int(offset)
    headers = {'Content-type': 'application/json'}
    for i in range((off-1)*10, off*10):
        r = requests.get("http://localhost:9200/test/_doc/"+str(i), headers = headers)
        # print(r.text)
        results["products"].append(r.json())
    return results

# @app.route("/products/<filter>")
# def getProductsFilter(filter):


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)