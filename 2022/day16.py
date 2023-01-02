import re
from collections import deque

#example
input = '''Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II'''.splitlines()

# with open('inputs/day16.txt', 'r') as file:
#     input = file.read().splitlines()

flow_rate = {}
neighbours = {}
for line in input:
    id, rate, tunnels = re.findall('Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)[0]
    flow_rate[id] = int(rate)
    neighbours[id] = tunnels.split(', ')

def nonzero_distances(start):

    output = {}
    queue = deque([(0, start)])
    visited = {start}

    while queue:
        distance, valve = queue.popleft()
        for neighbour in neighbours[valve]:
            if neighbour in visited:
                continue
            if flow_rate[neighbour] != 0:
                output[neighbour] = distance+1
            queue.append((distance+1, neighbour))
            visited.add(neighbour)
    
    return output

reduced_graph = {}
for valve, flow in flow_rate.items():
    if flow == 0 and valve != 'AA':
        continue
    reduced_graph[valve] = nonzero_distances(valve)

index = {}
for i, valve in enumerate(reduced_graph):
    index[valve] = i

cache = {}
def dfs(time, valve, bitmask):
    if (time, valve, bitmask) in cache:
        return cache[(time, valve, bitmask)]

    ans = 0
    for neighbour, distance in reduced_graph[valve].items():
        bit = 1 << index[neighbour]
        if bit & bitmask:
            continue
        time_remaining = time - distance - 1
        if time_remaining <= 0:
            continue
        ans = max(ans, dfs(time_remaining, neighbour, bitmask | bit) + time_remaining*flow_rate[neighbour])
    cache[(time, valve, bitmask)] = ans
    return ans

# part 1
print(dfs(30, 'AA', 0))


# part 2
b = (1 << len(reduced_graph)) - 1

m = 0

for i in range((b + 1) // 2):
    m = max(m, dfs(26, "AA", i) + dfs(26, "AA", b ^ i))

print(m)