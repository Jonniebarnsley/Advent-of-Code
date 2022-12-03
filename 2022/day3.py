with open('/Users/jonniebarnsley/Documents/Python/Advent of code/2022/day3.txt', 'r') as file:
    input = file.read()

rucksacks = input.split('\n')

priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def p1(input):
    ans = 0
    for rucksack in rucksacks:
        l = len(rucksack)
        c1 = rucksack[:int(l/2)]
        c2 = rucksack[int(l/2):]
        for item in c1:
            if item in c2:
                ans += priority.index(item)+1
                break
    return ans

def p2(input):
    ans = 0
    for n in range(int(len(rucksacks)/3)):
        elf1 = rucksacks[3*n]
        elf2 = rucksacks[3*n+1]
        elf3 = rucksacks[3*n+2]
        for item in elf1:
            if item in elf2 and item in elf3:
                ans += priority.index(item)+1
                break
    return ans

print(p1(input))
print(p2(input))
