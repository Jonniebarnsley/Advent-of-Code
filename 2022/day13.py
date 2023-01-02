from ast import literal_eval

with open('inputs/day13.txt', 'r') as file:
    input = file.read()

class identical(Exception): pass

def compare_ints(x, y):
    if x < y:
        return True
    if x > y:
        return False
    else:
        raise identical

def compare(A, B):

    for i in range(min(len(A), len(B))):

        if isinstance(A[i], int) and isinstance(B[i], int):
            try:
                return compare_ints(A[i], B[i])
            except identical:
                continue
        
        if isinstance(A[i], list) and isinstance(B[i], list):
            try:
                return compare(A[i], B[i])
            except identical:
                continue
        
        if isinstance(A[i], list) and isinstance(B[i], int):
            try:
                return compare(A[i], [B[i]])
            except identical:
                continue
        
        if isinstance(A[i], int) and isinstance(B[i], list):
            try:
                return compare([A[i]], B[i])
            except identical:
                continue

    if len(A) < len(B):
        return True
    elif len(A) > len(B):
        return False
    else:
        raise identical

# part 1
pairs = input.split('\n\n')

ans = []
for i, pair in enumerate(pairs):
    packet_A, packet_B = map(literal_eval, pair.split('\n'))
    if compare(packet_A, packet_B):
        ans.append(i+1)

print(sum(ans))

# part 2
packets = [line for line in input.splitlines() if line != '']
order = list(map(literal_eval, packets))

divider_1 = [[2]]
divider_2 = [[6]]
order.append(divider_1)
order.append(divider_2)

def bubble_sort(arr):
    flag = True
    while flag:
        flag = False
        for i in range(len(arr)-1):
            if not compare(arr[i], arr[i+1]):
                arr[i], arr[i+1] = arr[i+1], arr[i]
                flag = True
    return arr

sorted = bubble_sort(order)

a = b = 0
for i, packet in enumerate(sorted):
    if packet == divider_1:
        a = i+1
    if packet == divider_2:
        b = i+1
print(a*b)

