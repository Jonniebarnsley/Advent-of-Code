import re
from copy import deepcopy

with open('day5.txt', 'r') as file:
    input = file.read()

diagram, instructions = [part.splitlines() for part in input.split('\n\n')]

#turn diagram into lists
initial = []
for col in range(9):
    initial.append([])
    for line in reversed(diagram[:-1]):
        box = line[4*col+1]
        if box != ' ':
            initial[col].append(line[4*col+1])
        else:
            pass

def do_boxes(initial, crane_version):
    stacks = deepcopy(initial)
    for line in instructions:
        num, start, end = map(int, re.findall('\d+', line))

        #pick up boxes
        boxes = [stacks[start-1].pop() for _ in range(num)]

        #put down boxes
        if crane_version == 9000:
            for box in boxes:
                stacks[end-1].append(box)
        else:
            for box in reversed(boxes):
                stacks[end-1].append(box)
    return stacks


p1 = p2 = ''
p1_final = do_boxes(initial, crane_version = 9000)
p2_final = do_boxes(initial, crane_version = 9001)

for col in range(9):
    p1 += p1_final[col].pop()
    p2 += p2_final[col].pop()

print(p1)
print(p2)    