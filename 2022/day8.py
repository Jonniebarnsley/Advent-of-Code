input = '''30373
25512
65332
33549
35390'''.splitlines()

with open('inputs/day8.txt', 'r') as f:
    input = f.read().splitlines()

G = [[int(x) for x in line] for line in input]

l = len(G)
trees_on_boundary = 4*(l-1)

#part 1
def visible(x, y):
    h = G[x][y]
    if all (G[i][y]<h for i in range(x))\
        or all (G[i][y]<h for i in range(x+1, l))\
        or all (G[x][j]<h for j in range(y))\
        or all (G[x][j]<h for j in range(y+1, l)):
            return True
    else:
        return False

p1 = 0

#exterior
p1+=trees_on_boundary
#interior
for i in range(1, l-1):
    for j in range(1, l-1):
        if visible(i, j):
            p1+=1

print(p1)

#part 2
def north(x, y, h):
    if y == l-1:
        return 0
    elif G[x][y+1] < h:
        return 1+north(x, y+1, h)
    else:
        return 1

def south(x, y, h):
    if y == 0:
        return 0
    elif G[x][y-1] < h:
        return 1+south(x, y-1, h)
    else:
        return 1

def east(x, y, h):
    if x == l-1:
        return 0
    elif G[x+1][y] < h:
        return 1+east(x+1, y, h)
    else:
        return 1

def west(x, y, h):
    if x == 0:
        return 0
    elif G[x-1][y] < h:
        return 1+west(x-1, y, h)
    else:
        return 1

def scenic_score(x, y):
    h = G[x][y]
    n = north(x, y, h)
    s = south(x, y, h)
    e = east(x, y, h)
    w = west(x, y, h)
    return n*s*e*w


p2=0
for i in range(1, l-1):
    for j in range(1, l-1):
        ss = scenic_score(i, j)
        if ss > p2:
            p2 = ss

print(p2)