file = open("data 7.txt", "r")
pos = file.read()

data = [int(x) for x in pos.split(",")]

results = []
for x in range(2000):
    sum = 0
    for y in data:
        d = abs(x - y)

        #part 1
        #sum += d

        sum += d*(d+1)/2
    results.append(sum)

print(min(results))