with open('/Users/jonniebarnsley/Documents/Python/Advent of code/2022/day2.txt', 'r') as file:
    input = file.read()

rounds = [line.split() for line in input.split('\n')]

def score(round):
    total = 0
    them, me = round
    i = 'ABC'.index(them)
    j = 'XYZ'.index(me)
    total+=(j-i+1)%3*3
    total+=j+1
    return total

def translate(round):
    them, winlose = round
    i = 'ABC'.index(them)
    j = 'XYZ'.index(winlose)
    me = 'XYZ'[(i+j+2)%3]
    return (them, me)

p1 = p2 = 0
for round in rounds:
    p1 += score(round)
    p2 += score(translate(round))

print(p1)
print(p2)