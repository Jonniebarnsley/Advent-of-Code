import re
from itertools import combinations
import numpy as np

with open("day 19.txt", 'r') as file:
    input = file.read()

scanners_str = input.split("\n\n")
scanners = [np.array([list(map(int, p)) for p in re.findall("(-?\d+),(-?\d+),(-?\d+)", S)]) for S in scanners_str]

beacons = {tuple(p) for p in scanners[0]}

# create set of unique rotations in 3 dimensions

X = np.matrix('1 0 0; 0 0 1; 0 -1 0')
Y = np.matrix('0 0 -1; 0 1 0; 1 0 0')
Z = np.matrix('0 1 0; -1 0 0; 0 0 1')

l = []

for a in range(4):
    for b in range(4):
        for c in range(4):
            R = (X**a)*(Y**b)*(Z**c)
            l.append(R)

rotations = np.unique(l, axis = 0)

# function that attempts to match two beacon patterns

def compare(M, N):
    for q in N:
        for p in M:
            rel_pos = p - q
            test_map = {tuple(point + rel_pos) for point in N}
            if len(M & test_map) >= 12:
                return (True, rel_pos)
    return (False, None)

def prod(p, q):
    x1, y1, z1 = p
    x2, y2, z2 = q
    dist = abs((x2-x1)*(y2-y1)*(z2-z1))
    return dist

# create hashes for quick overlapping tests

hashes = [{prod(p, q): (p, q) for p, q in combinations(S, 2)} for S in scanners]

# create dictionary of matching scanners and their overlapping points

D = {0: [None, None, None, None, np.array([0, 0, 0])]}

while len(D) < len(scanners):
    for i in tuple(D):
        h1 = set(hashes[i])
        for j, h2 in enumerate(hashes):
            if i != j and not j in D:
                overlap = h1 & set(h2)
                if len(overlap) >= 66:
                    b1 = set()
                    b2 = set()
                    for d in overlap:

                        p, q = hashes[i][d]
                        b1.add(tuple(p))
                        b1.add(tuple(q))

                        r, s = hashes[j][d]
                        b2.add(tuple(r))
                        b2.add(tuple(s))
                        
                    D[j] = [i, b1, b2]

# add rotations and translations between scanner pairs to dictionary

for j in tuple(D)[1:]:
    i, b1, b2 = D[j]
    for r in rotations:
        rotated = [r.dot(p) for p in b2]
        success, t = compare(b1, rotated)
        if success:
            D[j].append(r)
            D[j].append(t)
            print("Found scanner "+str(j)+":", t)

# write all scanners with respect to scanner 0 

def rec(x):
    points_to, S1, S2, A, u = x
    points_beyond, S3, S4, B, v = D[points_to]
    if points_to == 0:
        return x
    else:
        x[4] = B.dot(u) + v
        x[3] = B.dot(A)
        x[0] = points_beyond
        return rec(x)

for i in tuple(D)[1:]:
    D[i] = rec(D[i])

# create map of all beacons

for k, S in enumerate(scanners[1:]):
    k = k+1
    points_to, S1, S2, r, t = D[k]
    new_set = {tuple(r.dot(p)+t) for p in S}
    beacons |= new_set

# part 2

def manhatten(p, q):
    x1, y1, z1 = p
    x2, y2, z2 = q
    dist = abs(x2-x1) + abs(y2-y1) + abs(z2-z1)
    return dist

def part2(D):
    scanner_locations = [D[i][4] for i in range(len(scanners))]
    ans = 0
    for p, q in combinations(scanner_locations, 2):
        d = manhatten(p, q)
        if d > ans:
            ans = d
    return ans

print(len(beacons))
print(part2(D))