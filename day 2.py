file = open("data 2.txt", 'r')

def convert(line):
    strip = line.rstrip()
    split = strip.split(" ")
    return split

commands = [convert(line) for line in file]

x=0
d=0
aim=0

for i in commands:
    if i[0] == "forward":
        x += int(i[1])
        d += aim*int(i[1])
    elif i[0] == "down":
        aim += int(i[1])
    else:
        aim -= int(i[1])

print(x*d)