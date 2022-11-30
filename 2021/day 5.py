import re

file = open("data 5.txt", 'r')

coords = re.findall("(\d+),(\d+) -> (\d+),(\d+)", file.read())

# part 1

# ver_or_hor = []

# for line in coords:
#     if line[0]==line[2] or line[1]==line[3]:
#         ver_or_hor.append(line)

grid = [[0 for i in range(1000)] for j in range(1000)]

for line in coords:
    x1, y1, x2, y2 = map(int, line)
    dx = x2 - x1
    dy = y2 - y1
    length = max(abs(dx), abs(dy))
    x_step = dx//length
    y_step = dy//length
    for k in range(length+1):
        grid[y1 + k*y_step][x1+k*x_step]+=1

count = 0

for line in grid:
    for coord in line:
        if coord > 1:
            count +=1

print(count)
