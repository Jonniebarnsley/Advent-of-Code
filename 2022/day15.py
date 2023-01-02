import re
from math import inf
import heapq

input = '''Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3'''.splitlines()

with open('inputs/day15.txt', 'r') as file:
    input = file.read().splitlines()

def manhatten(A, B):

    '''takes two coordinates and returns the manhatten distance between them'''

    x1, y1 = map(int, A)
    x2, y2 = map(int, B)
    distance = abs(y2-y1)+abs(x2-x1)
    return distance

data = []

for line in input:
    x, y, p, q = map(int, re.findall('-?\d+', line))
    sensor = (x, y)
    beacon = (p, q)
    distance = manhatten(sensor, beacon)
    data.append([sensor, beacon, distance])

def covered(intervals):
    min, max = intervals[0]
    for interval in intervals[1:]:
        start, end = interval
        if start > max+1:
            return (False, max+1)
        elif end > max:
            max = end
    if min <= 0 and max >= 4_000_000:
        return (True, None)
    else:
        return (False, None)

for row in range(4_000_000):
    intervals = []
    for sensor, _, distance in data:
        x, y = sensor
        dy = abs(y - row)
        if dy > distance:
            continue
        else:
            x_left = x - (distance - dy)
            x_right = x + (distance - dy)
            intervals.append((x_left, x_right))
    intervals.sort()
    cover, x = covered(intervals)
    if cover:
        continue
    else:
        print(x*4_000_000+row)
        break