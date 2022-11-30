import re

with open("data 13.txt", "r") as file:
    data = file.read()

input1 = re.findall("(\d+),(\d+)", data)
dots = [list(map(int, s)) for s in input1]

input2 = re.findall("(\w)=(\d+)", data)
dict = {"x": 0, "y": 1}
folds = [(dict[i[0]], int(i[1])) for i in input2]

for fold in folds:
    for dot in dots:
        d = max(0, dot[fold[0]]-fold[1])
        dot[fold[0]] -= 2*d

dots = set([tuple(x) for x in dots])

ans = ""
for j in range(6):
    for i in range(40):
        if (i, j) in dots:
            ans += "#"
        else:
            ans += " "
    ans += "\n"

print(ans)


