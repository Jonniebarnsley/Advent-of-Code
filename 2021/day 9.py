import numpy as np

def convert(line):
    strip = line.strip()
    integers = map(int, strip)
    return list(integers)

with open("data 9.txt", 'r') as file:
    nested_list = [convert(line) for line in file]

# test = "2199943210\n3987894921\n9856789892\n8767896789\n9899965678"
# nested_list = [list(map(int, line)) for line in test.split("\n")]

mat = np.array(nested_list)
print(mat)

sum = 0
low_points = []

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if i != 0:
            if mat[i][j] >= mat[i-1][j]:   #above
                continue
        if i != len(mat)-1:
            if mat[i][j] >= mat[i+1][j]:   #below
                continue
        if j != 0:
            if mat[i][j] >= mat[i][j-1]:   #left
                continue
        if j != len(mat[0])-1:
            if mat[i][j] >= mat[i][j+1]:   #right
                continue
        low_points.append((i, j))
        sum += mat[i][j]+1

print(sum)

def higher_points(point):
    higher_points = set()
    i, j = point[0], point[1]
    if i != 0:
        if mat[i][j] < mat[i-1][j] < 9:   #above
            higher_points.add((i-1, j))
    if i != len(mat)-1:
        if mat[i][j] < mat[i+1][j] < 9:   #below
            higher_points.add((i+1, j))
    if j != 0:
        if mat[i][j] < mat[i][j-1] < 9:   #left
            higher_points.add((i, j-1))
    if j != len(mat[0])-1:
        if mat[i][j] < mat[i][j+1] < 9:   #right
            higher_points.add((i, j+1))
    return higher_points

def higher_set(input):
    more_points = set()
    for point in input:
        even_more_points = higher_points(point)
        more_points = more_points | even_more_points
    return more_points

basin_sizes = []

for point in low_points:

    basin = set()
    start = {point}

    while True:
        basin = basin | start
        more_points = higher_set(start)
        if len(more_points)==0:
            break
        start = more_points

    basin_sizes.append(len(basin))

basin_sizes.sort(reverse = True)

answer = basin_sizes[0]*basin_sizes[1]*basin_sizes[2]

print(answer)
