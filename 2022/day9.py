import numpy as np

with open('inputs/day9.txt', 'r') as file:
    input = file.read().splitlines()

def untrunc(x):

    '''rounds up if x is positive and rounds down if x is negative. 
       i.e. the opposite of np.trunc(x)
    
    eg  0.5 -> 1
       -0.5 -> -1
       
       '''

    if x>0:
        return int(np.ceil(x))
    elif x<0:
        return int(np.floor(x))
    else:
        return 0

def move_rope(A, B):

    '''returns a vector by which to move a knot if it is not touching 
       the knot ahead of it in the rope'''

    dx, dy = B-A
    if abs(dx)>1 or abs(dy)>1:
        u = untrunc(dx/2)
        v = untrunc(dy/2)
        return np.array([u, v])
    else:
        return 0

def unit_vector(letter):

    '''matches U, D, L, R with corresponding unit vectors'''

    if letter == 'U':
        return [0, 1]
    elif letter == 'D':
        return [0, -1]
    elif letter == 'L':
        return [-1, 0]
    else:
        return [1, 0]

def solve(instructions, rope_length):

    '''does the thing'''

    rope = np.zeros((rope_length, 2))
    head = rope[0]
    tail = rope[rope_length-1]
    positions = {(0, 0)}

    for line in instructions:
        direction, distance = line.split()
        d = int(distance)
        s = unit_vector(direction)

        for _ in range(d):
            head += np.array(s)

            for i in range(1, rope_length):
                rope[i] += move_rope(rope[i], rope[i-1])

            positions.add(tuple(tail))

    return positions

p1 = solve(input, 2)
p2 = solve(input, 10)

print(len(p1))
print(len(p2))