import csv
import json

import pandas as pd
from flask_paginate import Pagination, get_page_parameter
from flask import Flask
from flask import render_template
from flask import request

#Paginação para o número de vestidos
ROWS_PER_PAGE = 10

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
@app.route("/capDressVal")
def get_json():
    with open("./cap.dress.val.json") as json_file:
        return json_file.read()


@app.route("/test")
def test():
    data = get_json()
    return render_template('test.html', data = json.dumps(data))

@app.route("/getPhoto/<name>")
def getPhoto(name):
    with open('data.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if (row[0].split(" ; ")[0] == str(name)):
                    print(str(row[0].split(" ; ")[1]))
                    return(str(row[0].split(" ; ")[1]))

@app.route('/getShop')
def colors():
    # Configurar paginação
    search = False
    q = request.args.get('q')
    if q:
        search = True

    page = request.args.get(get_page_parameter(), 1, type=int)
    """with open("./cap.dress.val copy.json") as json_file:
        val = ast.literal_eval(json_file)
        val1 = json.loads(json_file.read())
        val2 = val1['target'][0]['candidate'][0]['captions']
        table = pd.DataFrame(val1, columns=["target", "candidate", "captions"])"""
    data = get_json()
    print(data)
    pagination = Pagination(page=page, total=len(data), search = search)
    print(pagination)
    return render_template('dresses.html', dresses = data, pagination=pagination)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)