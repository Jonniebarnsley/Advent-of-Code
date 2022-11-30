import math

with open("data 18.txt", 'r') as file:
    input = file.read()

lines = input.split("\n")

def parse(line):
    level = 0
    L = []
    for i in list(line):
        if i == "[":
            level += 1
        elif i == "]":
            level -= 1
        elif i == ",":
            continue
        else:
            L.append([int(i), level])
    return L

def explode(L, i):
    if i > 0:
        L[i-1][0] += L[i][0]
    if i < len(L)-2:
        L[i+2][0] += L[i+1][0]
    L.pop(i)
    L[i][0] = 0
    L[i][1] -= 1

def split(L, i):
    L.insert(i+1, [math.ceil(L[i][0]/2), L[i][1]+1])
    L[i][0] = math.floor(L[i][0]/2)
    L[i][1] += 1

def reduce(L):
    while True:
        done = True
        for i, e in enumerate(L):
            if e[1] == 5:
                explode(L, i)
                done = False
                break
        if done:
            for i, e in enumerate(L):
                if e[0] > 9:
                    split(L, i)
                    done = False
                    break
        if done:
            break
    return L

def add(A, B):
    L = A+B
    for e in L:
        e[1] += 1
    reduce(L)
    return L

def mag(L):
    nest = 4
    while nest > 0:
        for i, e in enumerate(L):
            if e[1] == nest:
                L[i][0] = 3*L[i][0] + 2*L[i+1][0]
                L[i][1] -= 1
                L.pop(i+1)
        nest -= 1
    return L[0][0]

def part1(lines):
    L = parse(lines[0])
    for line in lines[1:]:
        parsed = parse(line)
        L = add(L, parsed)
    print(mag(L))

def part2(lines):
    ans = 0
    for x in lines:
        for y in lines:
            if x != y:
                X = parse(x)
                Y = parse(y)
                L = add(X, Y)
                m = mag(L)
                if m > ans:
                    ans = m
    print(ans)

part1(lines)
part2(lines)
