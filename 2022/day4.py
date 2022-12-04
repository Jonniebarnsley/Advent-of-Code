import re

with open('day4.txt', 'r') as file:
    input = file.read()

sections = [map(int, re.split(',|-', line)) for line in input.splitlines()]

p1 = p2 = 0
for a, b, c, d in sections:
    elf1 = set(range(a, b+1))
    elf2 = set(range(c, d+1))
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        p1+=1
    if len(elf1 & elf2) > 0:
        p2+=1

print(p1)
print(p2)