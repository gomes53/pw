from difflib import SequenceMatcher
import numpy as np

dictionary = open("dictionary.txt", "r").read().split("\n")

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def autocorrection (string):
    temp = []
    res = []
    n = []
    if string not in dictionary:
        for i in dictionary:
            ratio = similar(string, i)
            if ratio > 0.5:
                aux = [i, ratio]
                temp.append(aux)

        temp = np.array(temp)
        temp.sort(axis=0)
        for i in reversed(temp):
            res.append(i[0])
            n.append(i[1])
            if len(res) == 8:
                break


    print(res)
    print(n)

def test(string):
    size = len(string)

    res = []
    for i in dictionary:
        c = i[:size]
        if c == string and i.find(string) != -1:
            res.append(i)
        if len(res) > 10:
            break

    print(res)

#test("re")
autocorrection("dess")