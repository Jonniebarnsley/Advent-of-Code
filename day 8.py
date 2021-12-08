import re

with open("data 8.txt") as file:
    data = re.findall("(\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) (\w+) \| (\w+) (\w+) (\w+) (\w+)", file.read())

sum = 0

for line in data:
    inputs = ["".join(sorted(a)) for a in line[0:10]]
    outputs = ["".join(sorted(a)) for a in line[10:14]]
    inputs.sort(key=len)

    dic = {
        inputs[0]: 1,
        inputs[1]: 7,
        inputs[2]: 4,
        inputs[9]: 8
    }
    ivd = {v: k for k, v in dic.items()}

    len_5 = inputs[3:6]
    len_6 = inputs[6:9]

    for code in len_6:
        if all (letter in code for letter in ivd[4]):
            dic.update({code: 9})
        elif all (letter in code for letter in ivd[1]):
            dic.update({code: 0})
        else:
            dic.update({code: 6})
            ivd.update({6: code})

    for code in len_5:
        if all (letter in code for letter in ivd[1]):
            dic.update({code: 3})
        elif all (letter in ivd[6] for letter in code):
            dic.update({code: 5})
        else:
            dic.update({code: 2})
    
    final = "".join(str(dic[i]) for i in outputs)
    sum += int(final)

print(sum)

    