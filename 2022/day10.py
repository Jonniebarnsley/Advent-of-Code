with open('inputs/day10.txt', 'r') as file:
    input = file.read().splitlines()

cycle = 1
X = 1
line = 0
delay = True
p1 = []
screen = ['']*6

while cycle <= 240:

    #part 1
    if cycle in [20, 60, 100, 140, 180, 220]:
        p1.append(X*cycle)

    #part 2
    x = (cycle-1) % 40
    y = (cycle-1) // 40

    sprite = [X-1, X, X+1]
    if x in sprite:
        screen[y]+='#'
    else:
        screen[y]+=' '

    #execute instruction
    instruction = input[line]
    if instruction == 'noop':
        cycle += 1
        line += 1
    elif delay:
        cycle += 1
        delay = False
    else:
        V = instruction.split()[1]
        cycle += 1
        X += int(V)
        delay = True
        line += 1

print(sum(p1))

def print_screen(data):
    for line in data:
        print(''.join(line))

print_screen(screen)

