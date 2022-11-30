from collections import defaultdict
from math import inf
import heapq

with open("data 15.txt", "r") as file:
    input = file.read()

# input = """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581"""

lines = input.split("\n")
G = []
for line in lines:
    G.append([int(x) for x in list(line)])

N = len(G)

G2 = [[[] for i in range(5*N)] for j in range(5*N)]

for i in range(5*N):
    for j in range(5*N):
        G2[i][j] = G[i%N][j%N] + i//N + j//N
        if G2[i][j] > 9:
            G2[i][j] -= 9

def solve(G):

    M = len(G)
    Q = [(0, (0, 0))]

    min_dist = defaultdict(lambda: inf)

    while Q:
        total, pos = heapq.heappop(Q)

        x, y = pos
        if pos == (M-1, M-1):
            return total

        for (dx, dy) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            xx = x + dx
            yy = y + dy
            if 0<=xx<M and 0<=yy<M:
                new_total = total + G[xx][yy]

                if new_total < min_dist[(xx, yy)]:
                    heapq.heappush(Q, (new_total, (xx, yy)))
                    min_dist[(xx, yy)] = new_total

print(solve(G))
print(solve(G2))
