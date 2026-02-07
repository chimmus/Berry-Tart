# INSERT THINGS HERE, IDK WHAT TO PUT

map = {
    "0" : "00",
    "1" : "11",
    "2" : "10",
    "3" : "01"
}

map2 = {
    "A": "00",
    "B": "01",
    "C": "02",
    "D": "03",
    "E": "10",
    "F": "11",
    "G": "12",
    "H": "13",
    "I": "20",
    "J": "21",
    "K": "22",
    "L": "23",
    "M": "30",
    "N": "31",
    "O": "32",
    "P": "33"
}

ask = input("Decrypt? ")
d1 = ''
d2 = ''
d3 = ''
for char in ask:
    d1 += map2[char]
print(d1)

for char in d1:
    d2 += map[char]
print (d2)

d3 = ''.join(chr(int(d2[i:i+8], 2)) for i in range(0, len(d2), 8))

print(d3)