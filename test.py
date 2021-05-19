
def test(string):
    dictionary = open("dictionary.txt", "r").read().split("\n")

    res = []
    for i in dictionary:
        if i.find(string) != -1:
            res.append(i)
        if len(res) > 10:
            break

    print(res)

test("re")