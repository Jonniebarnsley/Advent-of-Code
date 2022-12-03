with open('/Users/jonniebarnsley/Documents/Python/Advent of code/2022/day3.txt', 'r') as file:
    input = file.read()

rucksacks = input.splitlines()

priority = '_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def p1(rucksacks):
    ans = 0
    for rucksack in rucksacks:
        l = len(rucksack)
        c1 = rucksack[:l//2]
        c2 = rucksack[l//2:]
        for item in c1:
            if item in c2:
                ans += priority.index(item)
                break
    return ans

def p2(rucksacks):
    ans = 0
    for n in range(0, len(rucksacks)-3, 3):
        elf1 = rucksacks[n]
        elf2 = rucksacks[n+1]
        elf3 = rucksacks[n+2]
        for item in elf1:
            if item in elf2 and item in elf3:
                ans += priority.index(item)
                break
    return ans

print(p1(rucksacks))
print(p2(rucksacks))
