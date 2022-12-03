input = '''1000
2000
3000

4000

5000
6000

7000
8000
9000

10000'''

with open('/Users/jonniebarnsley/Documents/Python/Advent of code/2022/day1.txt', 'r') as file:
    input = file.read()

max = 0
sec = 0
thd = 0

elves = input.split('\n\n')
for elf in elves:
    snacks = [int(x) for x in elf.split('\n')]
    calories = sum(snacks)
    if calories >= max:
        thd = sec
        sec = max
        max = calories
    elif calories >= sec:
        thd = sec
        sec = calories
    elif calories >= thd:
        thd = calories
    
print(max)
print(max+sec+thd)
