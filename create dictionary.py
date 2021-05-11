import json

file = open("./products/products_with_images_17k.json", 'rb').read()

transformed = json.loads(file)
dic = []

def magic(word, dic):
    temp = word.replace("/", " ").replace("(", " ").replace(")", " ")
    if word == temp:
        if word in dic:
            pass
        else:
            dic.append(word)
    else:
        temp = temp.split()

        for i in temp:
            magic(i, dic)


for i in transformed:
    for j in transformed[i]:
        temp = str(j["taxonomy"]).split()
        for k in temp:
            magic(k, dic)

with open("dictionary.txt", "w") as output:
    for i in dic:
        output.write('%s\n' % i)
