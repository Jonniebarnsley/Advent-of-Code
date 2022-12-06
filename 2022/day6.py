with open('day6.txt', 'r') as file:
    input = file.read()

def parse(signal, length):
    for i in range(length, len(signal)):
        chars = input[i-length:i]
        if len(set(chars)) == length:
            print(i)
            break

parse(input, 4)
parse(input, 14)