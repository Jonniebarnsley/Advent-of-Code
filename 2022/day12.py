import heapq
from math import inf
from itertools import product
from collections import defaultdict

with open('inputs/day12.txt', 'r') as file:
    input = file.read().splitlines()

X = len(input)
Y = len(input[0])
x_axis = range(X)
y_axis = range(Y)
coordinates = list(product(x_axis, y_axis))

def find_start():
    for (x, y) in coordinates:
        if input[x][y] == 'S':
            return (x, y)

def elevation(x, y):
    letter = input[x][y]
    if letter == 'S':
        return 0
    elif letter == 'E':
        return 25
    else:
        return ord(letter) - 97

def djikstra(start):

    heap = [(0, start)]
    heapq.heapify(heap)
    min_distance = defaultdict(lambda: inf)

    while heap:
        distance, (x, y) = heapq.heappop(heap)
        if input[x][y] == 'E':
            return min_distance[(x, y)]
        new_distance = distance + 1
        for (dx, dy) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            xx = x + dx
            yy = y + dy
            if not (0<=xx<X and 0<=yy<Y):
                continue
            if elevation(xx, yy) > elevation(x, y)+1:
                continue
            if new_distance < min_distance[(xx, yy)]:
                min_distance[(xx, yy)] = new_distance
                heapq.heappush(heap, (new_distance, (xx, yy)))

# part 1
start = find_start()
steps = djikstra(start)
print(steps)

# part 2
ans = inf
for (x, y) in coordinates:
    if input[x][y] != 'a':
        continue
    steps = djikstra((x, y))
    if steps == None:
        continue
    if steps < ans:
        ans = steps
print(ans)