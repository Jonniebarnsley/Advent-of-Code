file = open("data 1.txt", 'r')

def convert(line):
    strip = line.rstrip()
    integer = int(strip)
    return integer

depth = [ convert(line) for line in file ]

count = 0
sums=[]

for i in range(0, 1998):
    s = sum(depth[i:i+3])
    sums.append(s)

for j in range(0, 1997):
    if sums[j]<sums[j+1]:
        count += 1

print(count)
