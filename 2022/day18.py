import numpy as np
from itertools import product
from collections import deque

input = '''2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5'''.splitlines()

with open('inputs/day18.txt', 'r') as file:
    input = file.read().splitlines()

droplet = {tuple(map(int, line.split(','))) for line in input}
unit_vectors = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

# max dimensions of the droplet
X, Y, Z = map(max, zip(*droplet))

def draw_droplet(droplet):

    '''draw function for troubleshooting'''

    for c in range(Z+1):
        grid = np.full((X+1, Y+1), ' ')
        for x, y, z in droplet:
            if z == c:
                grid[x][y] = '#'
        for line in grid:
            print(''.join(line))

#test
#draw_droplet(cubes)

def surface_area(cube, object):

    '''returns the air-facing surface area (max 6) of a cube within a larger object'''

    x, y, z = cube
    count = 6
    for dx, dy, dz in unit_vectors:
        if (x+dx, y+dy, z+dz) in object:
            count-=1
    return count

# part 1
p1 = sum(surface_area(cube, droplet) for cube in droplet)
print(p1)

# part 2
def bfs(start, boundaries):

    ''' BFS algorithm that returns a set of all coordinates accessible from a start point
        without passing through any boundaries'''

    queue = deque([start])
    visited = set()

    while queue:

        x, y, z = queue.popleft()
        for dx, dy, dz in unit_vectors:
            xx, yy, zz = x+dx, y+dy, z+dz
            if (xx, yy, zz) in boundaries:
                continue
            if (xx, yy, zz) in visited:
                continue
            if not (-1<=xx<=X+1 and -1<=yy<=Y+1 and -1<=zz<=Z+1):
                continue
            queue.append((xx, yy, zz))
            visited.add((xx, yy, zz))
            
    return visited

start = (-1, -1, -1)
outside = bfs(start, droplet)

# fill in droplet by adding all cubes not accessible by steam to the set 
for cube in product(range(X), range(Y), range(Z)):
    if cube in droplet:
        continue
    if cube in outside:
        continue
    droplet.add(cube)

p2 = sum(surface_area(cube, droplet) for cube in droplet)
print(p2)