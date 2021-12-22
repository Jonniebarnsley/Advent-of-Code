from collections import deque
import math

input = "04005AC33890"

with open("data 16.txt", "r") as file:
    input = file.read()

num = bin(int("1"+input, 16))[3:]

d = deque(list(str(num)))

def popn(d, n):
    list = []
    for i in range(n):
        x = d.popleft()
        list.append(x)
    return list

p1 = 0

def parse(data):
    global p1
    v = popn(data, 3)
    version = int("".join(v), 2)
    p1 += version
    t = popn(data, 3)
    typeid = int("".join(t), 2)

    if typeid == 4:    #literal value
        x = 1
        l = []
        while x == 1:
            x = int(data.popleft())
            d4 = popn(data, 4)
            l += d4
        lit = int("".join(l), 2)
        return lit

    else:    #operator
        values = []
        lenid = int(data.popleft())

        if lenid == 0:
            l = popn(data, 15)
            bitlen = int("".join(l), 2)
            x = len(data)
            while len(data)>x-bitlen:
                p = parse(data)
                values.append(p)
        else:
            l = popn(data, 11)
            n = int("".join(l), 2)
            for i in range(n):
                p = parse(data)
                values.append(p)
        
        if typeid == 0:    #sum
            return sum(values)

        if typeid == 1:    #product
            return math.prod(values)

        if typeid == 2:    #min
            return min(values)

        if typeid == 3:    #max
            return max(values)

        if typeid == 5:    #greater than
            return 1 if values[0] > values[1] else 0

        if typeid == 6:    #less than
            return 1 if values[0] < values[1] else 0
        
        if typeid == 7:    #equal to
            return 1 if values[0] == values[1] else 0

ans = parse(d)
print(p1)
print(ans)
