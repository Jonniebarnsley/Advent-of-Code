file = open("data 6.txt", "r")
input = file.read()

list = list(map(int, input.split(",")))

# part 1

# for n in range(256):
#     for i, fish in enumerate(list):
#         if fish == 0:
#             list[i] +=6
#             list.append(9)
#         else:
#             list[i] -= 1

# print(len(list))

counts = [list.count(i) for i in range(9)]

for n in range(256):
    previous = counts[:]
    for i, group in enumerate(counts):
        if i != 6 and i != 8:
            counts[i] = previous[i+1]
        else:
            counts[6] = previous[7]+previous[0]
            counts[8] = previous[0]
    
print(sum(counts))
