import re

input = "target area: x=265..287, y=-103..-58"

findnum = re.findall("-?\d+", input)
coords = list(map(int, findnum))

x1, x2, y1, y2 = coords

def attempt(u, v):
    pos = x, y = [0, 0]
    success = False
    max = int(v*(v+1)/2)
    while x<x2 and y>y1:
        x += u
        y += v
        u -= 1 if u>0 else 0
        v -= 1
        
        if x1 <= x <= x2 and y1 <= y <= y2:
            success = True
            break
        
    return (success, max)

p1 = 0
p2 = 0
for u in range(300):
    for v in range(-120, 300):
        a = attempt(u, v)
        if a[0]:
            p2 += 1
            if a[1]>p1:
                p1 = a[1]

print(p1)
print(p2)
