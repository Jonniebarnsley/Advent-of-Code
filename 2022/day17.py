import numpy as np

input = '>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>'

# with open('inputs/day17.txt', 'r') as file:
#     input = file.read()

solid = {(x, 0) for x in range(7)}

class Rock():
    def __init__(self, coords: np):
        self.shape = coords
        self.width = None

a = Rock(np.array([(0, 0), (1, 0), (2, 0), (3, 0)]))
b = Rock(np.array([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]))
c = Rock(np.array([(2, 0), (2, 1), (2, 2), (1, 0), (0, 0)]))
d = Rock(np.array([(0, 0), (0, 1), (0, 2), (0, 3)]))
e = Rock(np.array([(0, 0), (1, 0), (0, 1), (1, 1)]))

rocks = [a, b, c, d, e]

for rock in rocks:
    rock.width = max(x for (x, y) in rock.shape)

def draw_rocks(solids, falling_shape):
    X = 8
    Y = max(y for (x, y) in solids)+1
    grid = np.full((Y+1, X+1), ' ')
    for y in range(Y+1):
        grid[y][0] = '|'
        grid[y][X] = '|'
    for (x, y) in falling_shape:
        grid[Y-y][x+1] = '@'
    for (x, y) in solids:
        grid[Y-y][x+1] = '#'
    for line in grid:
        print(''.join(line))
    print()

solid = {(x, 0) for x in range(7)}
input_length = len(input)
count_rocks = 0
height = 0
index = 0
increase_by = []
while count_rocks < 2022:
    x, y = 2, height+4
    rock = rocks[count_rocks%5]
    at_rest = False
    while not at_rest:
        shape = [np.array([x, y])+coord for coord in rock.shape]
        direction = input[index%input_length]
        if direction == '>' \
        and x+rock.width < 6 \
        and all((p+1, q) not in solid for (p, q) in shape):
            x+=1
        if direction == '<' \
        and x > 0 \
        and all((p-1, q) not in solid for (p, q) in shape):
            x-=1
        shape = [np.array([x, y])+coord for coord in rock.shape]
        if all((p, q-1) not in solid for (p, q) in shape):
            y-=1
        else:
            solid |= {tuple((p, q)) for p, q in shape}
            at_rest = True
            count_rocks += 1
            increase = max(height, max(q for (p, q) in shape)) - height
            increase_by.append(increase)
            height = max(height, max(q for (p, q) in shape))
            #draw_rocks(solid, shape)
        index+=1

print(height)

digits = increase_by[200:]

def find_repeating_pattern(lst):
  # Initialize a variable to keep track of the longest repeating pattern found so far
  longest_pattern = []
  # Iterate over sublists of increasing length
  for length in range(1, len(lst)):
    # Iterate over sublists of the current length
    for i in range(len(lst) - length + 1):
      sublist = lst[i:i+length]
      # Check if the sublist repeats within the list
      if lst[i+length:i+2*length] == sublist:
        # Update the longest repeating pattern if necessary
        if len(sublist) > len(longest_pattern):
          longest_pattern = sublist
  return longest_pattern

print(len(find_repeating_pattern(digits)))