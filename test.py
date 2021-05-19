from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def test(string):
    dictionary = open("dictionary.txt", "r").read().split("\n")
    size = len(string)

    res = []
    for i in dictionary:
        c = i[:size]
        if c == string and i.find(string) != -1:
            res.append(i)
        if len(res) > 10:
            break

    print(res)

test("re")