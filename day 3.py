file = open("data 3.txt", 'r')

data = [line.rstrip() for line in file]

# part 1

# gamma= ""
# epsilon = ""

# for j in range(12):
#     total = sum(int(i[j]) for i in data)
    
#     if total > len(data)/2:
#         gamma += "1"
#         epsilon += "0"

#     else:
#         gamma += "0"
#         epsilon += "1"

# print(int(gamma, 2)*int(epsilon, 2))

lsr = data[:]
ogr = data[:]

for j in range(12):
    total = sum(int(i[j]) for i in lsr)
    
    if total >= len(lsr)/2:
        winner = "1"
    else:
        winner = "0"

    lsr = [i for i in lsr if i[j] == winner]

    if len(lsr)==1:
        break

for j in range(12):
    
    total = sum(int(i[j]) for i in ogr)
    
    if total < len(ogr)/2:
        winner = "1"
    else:
        winner = "0"
    
    ogr = [i for i in ogr if i[j] == winner]

    if len(ogr)==1:
        break
    
a = int(lsr[0], 2)
b = int(ogr[0], 2)

print(a*b)