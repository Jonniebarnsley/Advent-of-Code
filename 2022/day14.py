import numpy as np

with open('inputs/day14.txt', 'r') as file:
    input = file.read()

coords = [[tuple(map(int, coord.split(','))) for coord in line.split(' -> ')]\
                                            for line in input.splitlines()]

def line_between(A, B):

    '''takes two coordinates A and B and returns a list of coordinates
       between A and B. Excludes the end point, which we will add on later'''

    x1, y1 = A
    x2, y2 = B
    dx = x2 - x1
    dy = y2 - y1
    l = max(abs(dx), abs(dy))
    unit_vector = np.array([dx, dy]) // l
    line = []
    start = np.array(A)
    for i in range(l):
        point = tuple(start + i*unit_vector)
        line.append(point)
    return line

def make_boundaries(data):

    '''takes the input and returns a set of coordinates occupied by the
       boundaries'''

    boundaries = set()
    for route in data:
        for i in range(len(route)-1):
            A = route[i]
            B = route[i+1]
            for point in line_between(A, B):
                boundaries.add(point)
        boundaries.add(route[-1]) # end point
    return boundaries

def find_bottom(data):

    '''takes the input and finds the lowest coordinate occupied by a boundary 
       point - useful for determining the floor depth or when a grain of sand 
       has fallen into the abyss'''

    y_max = 0
    for line in data:
        for coord in line:
            y  = coord[1]
            if y > y_max:
                y_max = y
    return y_max


def do_sand(coords, floor = False):

    '''simulates the falling sand for a given input. Returns the
       number of grains that have come to rest before the break
       clause has been reached:
       
       part 1: When a grain of sand falls into the abyss
       part 2: When a grain of sand comes to rest at (500, 0)
       
       '''

    solid = make_boundaries(coords)
    bottom = find_bottom(coords)

    x = 500
    y = 0
    grains_at_rest = 0
    while True:
        
        if y > bottom: # grain has reached abyss/floor
            if not floor: # part 1
                return grains_at_rest
            else: # part 2
                solid.add((x, y))
                grains_at_rest += 1
                x = 500
                y = 0
                continue
        
        # if not at the abyss/floor, the grain falls
        if (x, y+1) not in solid: # below
            y+=1
        elif (x-1, y+1) not in solid: # below and left
            x-=1
            y+=1
        elif (x+1, y+1) not in solid: # below and right
            x+=1
            y+=1
        else:
            solid.add((x, y))
            grains_at_rest += 1
            if (x, y) == (500, 0): # part 2 break clause
                return grains_at_rest
            else:
                x = 500
                y = 0

print(do_sand(coords, floor=False))
print(do_sand(coords, floor=True))