import random
import math

# this function is used to find number of  pairs of queens that don't threaten each other
def find_value(array):
    value = 0
    for i in range(0, 9):
        for j in range(i, 9):
            if array[i] != array[j] and abs(array[i] - array[j]) != abs(i - j):
                value += 1

    return value


# In each state we store an array called position its length is 9 and position[i] is
# the row index of  the queen in the ith column. and h is equal to the number of queens that don't threaten each other
class State:
    def __init__(self, position, h):
        self.position = position
        self.good_couples = h


# Problem class is used to generate a random initiate state.
class Problem:
    def __init__(self):
        self.po = []
        for i in range(0, 9):
            self.po.append(random.randint(0, 8))
        self.init_state = State(self.po, find_value(self.po))


# In this function we create all the children of current that are different from current only in positions
# of one of the queens in its column
def highest_value_successor(current):
    max = 0
    global new_li
    global best_child
    for i in range(0, 9):
        for j in range(0, 9):
            if j != current.position[i]:
                new_li = current.position[:]
                new_li[i] = j
                h = find_value(new_li)
                if h > max:
                    max = h
                    best_child = State(new_li, h)
    return best_child


# If we find a better child we continue our search, if there is not we return the current state
# level tell us how many step we need to find the local maximum
def hill_climbing(problem):
    current = problem.init_state
    level = 0
    while True:
        neighbor = highest_value_successor(current)
        if neighbor.good_couples <= current.good_couples:
            return current, level
        level += 1
        current = neighbor


# An auxiliary function to print the chess board. queens are shown by 1
def print_answer(answer):
    array = [[0 for x in range(9)] for y in range(9)]
    for i in range(0, 9):
        for j in range(0, 9):
            if answer.position[i] == j:
                array[j][i] = 1

    for i in range(0, 9):
        for j in range(0, 9):
            print(array[i][j], end="")
        print("")


# By this function we run hill climbing function 20 runs, then we calculate how many of them is the answer
def repeat_until_you_get():
    total = 0
    good_board = 0
    for i in range(0,20):
        problem = Problem()
        answer, level = hill_climbing(problem)
        if answer.good_couples == 36:
            good_board += 1
        total += level
    print("in ", good_board*5, "% we found the answer")
    print("in average we need ", math.ceil(total/20), " levels to find the answer")


problem = Problem()
print(problem.init_state.position)
answer, level = hill_climbing(problem)
print(answer.position)
print_answer(answer)
print(answer.good_couples)
repeat_until_you_get()

