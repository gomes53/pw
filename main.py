from flask import Flask, jsonify
from flask import request
from flask import render_template
from elasticsearch import Elasticsearch
from difflib import SequenceMatcher
# import gensim.downloader as api
import numpy as np
import json
import csv
import sys
import re
import operator
import requests

es = Elasticsearch()
app = Flask(__name__)

# wv = api.load('word2vec-google-news-300')

dictionary = open("dictionary.txt", "r").read().split("\n")


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


@app.route("/")
def index():
    return render_template('/index.html')


@app.route("/shop/<type>/<offset>")
def shop(offset, type):
    return render_template('/shop_test.html')


@app.route("/product_details.html")
def details():
    return render_template('/product_details.html')


@app.route("/test")
def test():
    return render_template('test.html')


@app.route("/products/<type>/<offset>")
def getProductsOffset(offset, type):
    results = {"products": []}
    off = int(offset)
    headers = {'Content-type': 'application/json'}
    for i in range((off - 1) * 10, off * 10):
        r = requests.get("http://localhost:9200/" + type + "/_doc/" + str(i), headers=headers)
        results["products"].append(r.json())
    return results


@app.route("/refine/<currentIndex>/<filter>")
def refineSearch(currentIndex, filter):
    headers = {'Content-type': 'application/json'}
    taxList = []
    ids = []
    prevQuery = request.args.get("f" + str(0))
    print(prevQuery)
    for i in range(1, len(request.args)):
        ids.append(request.args.get("f" + str(i)))
        print(i)

    unwanted_chars = ".,-&"
    wordfreq = {}

    for i in range(3):
        id = ids[i]
        req = requests.get('http://localhost:9200/' + currentIndex + '/_doc/' + id, headers=headers)
        js = json.loads(req.text)
        taxonomy = js["_source"]["taxonomy"]
        words = re.findall(r"[\w']+", taxonomy)
        taxList.append(words)
        for raw_word in words:
            word = raw_word.strip(unwanted_chars)
            if word not in wordfreq:
                wordfreq[word] = 0
            wordfreq[word] += 1

    orderedDict = dict(sorted(wordfreq.items(), key=lambda item: item[1]))
    queryWords = []
    for i in range(1, 3):
        queryWords.append(list(orderedDict.items())[-i][0])

    newQuery = " ".join(queryWords)
    print(prevQuery + " " + newQuery)

    return getProductsFilter(currentIndex, filter, prevQuery, newQuery, 0, 10000)


# example: filter/dresses/taxonomy/red/0/1000
@app.route("/filter/<currentIndex>/<filter>/<text>/<boostedText>/<minPrice>/<maxPrice>")
def getProductsFilter(currentIndex, filter, text, boostedText, minPrice, maxPrice):
    print("entrei")
    results = {"products": []}
    print("boostedtext " + boostedText)

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
                    "must": {
                        "bool": {
                            "should": [
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
                                        str(filter): str(text)
                                    }
                                }
                            ]
                        }
                    }
                }
            }
        }

    res = es.search(index=currentIndex, body=body)

    for i in res["hits"]["hits"]:
        results["products"].append(i)

    return jsonify(results)


@app.route("/search/dictionary")
def dict():
    return jsonify(dictionary)


"""
Para este método assume-se que a search consiste de uma pesquisa simples, como 
'dress' ou 'blue dress'

O método transforma a string num array de strings

retorna um json com todas as palavras contidas no dicionário que se relacionam com 
esse conjunto de palavras e contenham um score acima de um valor
"""


@app.route("/filter/searchBar/<search>")
def sugested(search):
    results = {"products": []}


#     searchVector = search.split()

#     top = wv.most_similar(positive=searchVector, topn=30)

#     for i in top:
#         if i[0] in dictionary and i[1] > 0.4:
#             results["products"].append(i[0])
#         else:
#             pass

#     return jsonify(results)

"""
Objetivo é ser utilizado para completar as pesquisas do
utilizador, ou seja, autocomplition
"""


@app.route("/filter/searchBar/aux/<search>", methods=['GET'])
def autocomplition(search):
    results = {"products": []}
    size = len(search)

    for i in dictionary:
        c = i[:size]
        if c == search and i.find(search) != -1:
            results["products"].append(i)
        if len(results["products"]) > 5:
            break

    return jsonify(results)


"""
O autocorrection é utilizado no final da escrita de uma palavra e 
caso esta não esteja present no dicionário, o sistema irá sugerir as
5 palavras com melhor score presente no dicionário
"""


@app.route("/filter/searchBar/correction/<search>")
def autocorrection(search):
    temp = []
    results = {"products": []}

    print(search)

    if search not in dictionary:
        for i in dictionary:
            ratio = similar(search, i)
            if ratio > 0.5:
                aux = [i, ratio]
                temp.append(aux)

        temp = np.array(temp)
        temp.sort(axis=0)
        for i in reversed(temp):
            results["products"].append(i[0])
            if results["products"] == 5:
                break

    return jsonify(results)


@app.route("/testing/example")
def testing():
    """results = {"products": []}

    top = wv.most_similar(positive=["lipstick", "red"], negative=["eyeliner"]) [0][0]

    for i in top:
        if i[0] in dictionary:
            results["products"].append(i[0])
        else:
            pass

    return jsonify(results)"""


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
