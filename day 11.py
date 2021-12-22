input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

lines = input.split("\n")
G = []
for line in lines:
    G.append([int(x) for x in line])

H = len(G)
W = len(G[0])

def increment(G):
    for i in range(W):
        for j in range(H):
            G[j][i]+=1

def flash(x, y):
    global ans
    global count
    ans += 1
    count += 1
    G[x][y] = 0
    for dx in  [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            xx = x+dx
            yy = y+dy
            if 0<=xx<W and 0<=yy<H and G[xx][yy] != 0:
                G[xx][yy] += 1
                if G[xx][yy] > 9:
                    flash(xx, yy)

ans = 0
t = 0
while True:

    t += 1
    count = 0
    increment(G)

    for i in range(W):
        for j in range(H):
            if G[i][j] > 9:
                flash(i, j)

    if t == 100:
        print(ans)

    if count == H*W:
        break

print(t)

new_lines = []
for line in G:
    joined = "".join(map(str, line))
    new_lines.append(joined)
final = "\n".join(new_lines)

print(final)