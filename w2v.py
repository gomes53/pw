"""
Códico puramente para teste
"""


import gensim.downloader as api

wv = api.load('word2vec-google-news-300')

top = wv.most_similar(positive=["dress"], topn=20)

dictionary = open("dictionary.txt", "r").read().split("\n")
res = []
vals = []

print("Started:")
for i in top:
    if i[0] in dictionary:
        res.append(i[0])
        vals.append(i[1])
        print(i[0], "accepted!")
    else:
        print(i[0], "denied!")

print(res)
print(vals)