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

list = []

for a in range(4):
    for b in range(4):
        for c in range(4):
            R = (X**a)*(Y**b)*(Z**c)
            list.append(R)

rotations = np.unique(list, axis = 0)

# function that attempts to match two beacon patterns

def compare(M, N):
    global beacons
    success = False
    for q in N:
        for p in M:
            rel_pos = p - q
            test_map = {tuple(p + rel_pos) for p in N}
            if len(beacons & test_map) >= 10:
                beacons = beacons | test_map
                success = True
                break
        if success:
            break
    return (success, rel_pos)

# part 1

while len(scanners) > 1:
    j = 0
    for i, S in enumerate(scanners[1:]):
        for r in rotations:
            map = [r.dot(p) for p in S]
            done, pos = compare(beacons, map)
            if done:
                scanners.pop(i+1-j)  # j adjusts index for scanners already popped this cycle
                j+=1
                print(pos)
                break

# part 2

p2 = 0
for (P, Q) in list(combinations(beacons, 2)):

    x1, y1, z1 = P
    x2, y2, z2 = Q
    dist = abs(x2 - x1) + abs(y2 - y1) + abs(z2 - z1)
    if dist > p2:
        p2 = dist

print(len(beacons))
print(p2)