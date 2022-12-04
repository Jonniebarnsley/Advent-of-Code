import re

with open('day4.txt', 'r') as file:
    input = file.read()

pairs = input.splitlines()

p1 = p2 = 0
for pair in pairs:
    x1, y1, x2, y2 = map(int, re.split(',|-', pair))
    elf1 = set(range(x1, y1+1))
    elf2 = set(range(x2, y2+1))
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        p1+=1
    if len(elf1 & elf2) > 0:
        p2+=1

print(p1)
print(p2)