with open('/Users/jonniebarnsley/Documents/Python/Advent of code/2022/day1.txt', 'r') as file:
    input = file.read()

top3 = [0, 0, 0]

elves = input.split('\n\n')
for elf in elves:
    snacks = [int(x) for x in elf.splitlines()]
    calories = sum(snacks)
    if calories >= top3[2]:
        top3.pop()
        top3.append(calories)
        top3.sort(reverse=True)

p1 = top3[0]
p2 = sum(top3)

print(p1)
print(p2)
