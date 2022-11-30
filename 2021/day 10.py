with open("data 10.txt", "r") as file:
    input = file.read()

# input = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]"""

lines = input.split("\n")

openers = ["[", "(", "{", "<"]
closers = ["]", ")", "}", ">"]

corrupt_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
complete_scores = {")": 1, "]": 2, "}": 3, ">": 4}

p1_total = 0
p2_scores = []

for line in lines:
    corrupted = False
    legal = []

    for element in line:
        if element in openers:
            i = openers.index(element)
            legal.append(closers[i])
        else:
            if element == legal[-1]:
                legal.pop()
                continue
            else:
                p1_total += corrupt_scores[element]
                corrupted = True
                break
    
    if corrupted:
        continue

    score = 0
    legal.reverse()
    for element in legal:
        score = 5*score + complete_scores[element]
    p2_scores.append(score)

p2_scores.sort()
p2 = p2_scores[int((len(p2_scores)-1)/2)]

print("part 1:", p1_total)
print("part 2:", p2)
