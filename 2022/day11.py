import re
import copy
import numpy
from collections import deque

with open('inputs/day11.txt') as file:
    input = file.read()

class Monkey():

    '''A monkey object with the following attributes:
    
        items:              A list of worry scores for each item the monkey is holding
        operation:          The unique operation the monkey applies when inspecting an item
        divisor:            The number by which the monkey divides when testng each item
        pass/fail targets:  The number of the monkey the item will be passed to if the test passes or fails
        score:              Keeps track of the number of times a monkey has inspected an item
                           
    '''

    def __init__(self, 
                 starting_items: list,  #e.g. [79, 64] 
                 operation: callable,   #e.g. f: x -> x+3
                 divisor: int,          #e.g. 23
                 pass_target: int,      #e.g. 3
                 fail_target: int       #e.g. 1
                 ):

        self.items = starting_items
        self.operation = operation
        self.divisor = divisor
        self.PASS = pass_target
        self.FAIL = fail_target
        self.score = 0

    def inspect(self, item, relief=True):

        '''inspects an item and applies the appropriate operations, depending
           on which part we are solving.'''

        inspected = self.operation(item)

        if relief: #part 1
            inspected //= 3
        else: #part 2
            inspected %= magic_number

        self.items[0] = inspected
        self.score += 1

        return inspected
    
    def throw(self, item, target):

        '''removes an item (always the leftmost) from the monkey and adds it to the
           target monkey as the rightmost item'''

        self.items.popleft()
        target.items.append(item)

def parse(input):

    '''returns a list of monkeys with the attributes described in the input'''

    output = []
    for section in input.split('\n\n'):
        lines = section.splitlines()

        starting_items = deque(map(int, re.findall('\d+', lines[1])))

        operation = lines[2].split(' = ')[1]
        def inspect(old, operation = operation):
            return eval(operation)

        divisor = int(re.search('\d+', lines[3]).group(0))

        pass_target = int(re.search('\d', lines[4]).group(0))
        fail_target = int(re.search('\d', lines[5]).group(0))

        output.append(Monkey(starting_items, inspect, divisor, pass_target, fail_target))
    
    return output

def monkey_business(monkeys):

    '''calculates the monkey business score, i.e. the product of the two highest-scoring
       monkeys according to the number of items inspected'''

    scores = [monkey.score for monkey in monkeys]
    scores.sort(reverse = True)
    ans = scores[0]*scores[1]
    return ans

def solve(monkeys, no_of_rounds, relief=True):

    '''the monkeys throw items around for a specified number of rounds, with a 'relief'
       parameter to determine which part of the problem we are solving (default part 1).
       
       Returns the final monkey business score, a.k.a. our answers'''

    round = 1
    while round <= no_of_rounds:
        for monkey in monkeys:
            for item in monkey.items.copy():
                item = monkey.inspect(item, relief)
                if item % monkey.divisor == 0:
                    target = monkeys[monkey.PASS]
                else:
                    target = monkeys[monkey.FAIL]
                monkey.throw(item, target)
        round += 1

    return monkey_business(monkeys)

monkeys = parse(input)
magic_number = numpy.product([monkey.divisor for monkey in monkeys])
p1 = solve(copy.deepcopy(monkeys), no_of_rounds = 20)
p2 = solve(monkeys, no_of_rounds = 10000, relief=False)

print(p1)
print(p2)