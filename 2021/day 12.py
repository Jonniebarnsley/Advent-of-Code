import re
from collections import defaultdict

with open("data 12.txt", "r") as file:
    input = file.read()

pairs = re.findall("(\w+)-(\w+)", input)

D = defaultdict(list)
for a, b in pairs:
    D[a] += [b]
    D[b] += [a]

routes = [["start"]]
complete = []

def branch(list):
    next = []
    for route in list:
        twice = False
        for a in route:
            if a.islower() and route.count(a) == 2:
                twice = True
        for e in D[route[-1]]:
            if e == "start":
                continue
            elif e == "end":
                complete.append(route+[e])
            elif e.isupper() or e not in route or not(twice):
                next.append(route+[e])
    return next

while len(routes)>0:
    routes = branch(routes)

print(len(complete))
