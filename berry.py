# IDK WHAT TO PUT HERE

import clipboard as c

map = {
    "00" : 0,
    "11" : 1,
    "10" : 2,
    "01" : 3,
}

map2 = {
    "00": "A",
    "01": "B",
    "02": "C",
    "03": "D",
    "10": "E",
    "11": "F",
    "12": "G",
    "13": "H",
    "20": "I",
    "21": "J",
    "22": "K",
    "23": "L",
    "30": "M",
    "31": "N",
    "32": "O",
    "33": "P",
}

stringed = ""
numbers = ""

def binary(c):
    temp = ""
    temp = "".join(format(ord(char), "08b") for char in c)
    print(temp)
    return temp

ask = input("String? ")
binary(ask)

bins = binary(ask)





numbers = [map[bins[i:i+2]] for i in range(0, len(bins), 2)]
stringed = "".join(str(n) for n in numbers)

print(stringed)

if (len(stringed) % 2) == 1:
    stringed += "0"


numbers2 = [map2[stringed[i:i+2]] for i in range(0, len(stringed), 2)]
letters = "".join(str(n) for n in numbers2)

c.copy(letters)

print(letters)