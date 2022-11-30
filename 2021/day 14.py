import re
from collections import defaultdict

with open("data 14.txt", "r") as file:
    input = file.readline().strip()
    pairs = file.read()

# print(input)

# input = "NNCB"

# pairs = """CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C"""

r = re.findall("(\w+) -> (\w)", pairs)
D = defaultdict(str)
for x, y in r:
    D[x] += y

adj = set([d for d in D])
el = set([D[d] for d in D])

A = defaultdict(int)
for a in adj:
    if a in input:
        A[a] += input.count(a)
    else:
        A[a] = 0

E = defaultdict(int)
for e in input:
    E[e] += 1

for i in range(40):
    AA = defaultdict(int)
    for a in A:
        AA[a[0]+D[a]] += A[a]
        AA[D[a]+a[1]] += A[a]
        E[D[a]] += A[a]
    A = AA



# def polymerise(input):
#     list = []
#     for i in range(len(input)-1):
#         list.append(input[i:i+2])

#     for i, e in enumerate(list):
#         list[i] = e[0]+D[e]
#     return "".join(list)+input[-1]

# print(polymerise(input))

# for i in range(10):
#     input = polymerise(input)

# count = defaultdict(int)
# for i in input:
#     count[i]+=1



x = [E[e] for e in E]
x.sort()


print(x[-1]-x[0])
