import random
import math

class State:
    def __init__(self, position, h):
        self.position = position
        self.bad_couples = h

# here we calculate the number of pairs of queens that threaten each other so
# value is better when it is near 0
def find_value(array):
    value = 0
    for i in range(0, 9):
        for j in range(i+1, 9):
            if array[i] == array[j] or abs(array[i] - array[j]) == abs(i - j):
                value += 1

    return value


class Problem:
    def __init__(self):
        self.po = []
        for i in range(0, 9):
            self.po.append(random.randint(0, 8))
        self.init_state = State(self.po, find_value(self.po))


# In this function we just create a random child that is different from current in the row of one of the queens
def random_selected_successor(current):
    i = random.randint(0, 8)
    j = random.randint(0, 8)
    new_li = current.position[:]
    while j == current.position[i]:
        j = random.randint(0, 8)
    new_li[i] = j
    next = State(new_li, find_value(new_li))

    return next


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


# In this cooling_rate is used to do schedules function
def simulated_annealing(problem):
    current = problem.init_state
    level = 0
    t = 0
    T = 1000000  # Initial temperature
    cooling_rate = 0.999  # Cooling rate

    # Until T is greater than a threshold get a random child
    while T > 0.1:
        t += 1
        next_state = random_selected_successor(current)
        delta_E = current.bad_couples - next_state.bad_couples

        if delta_E > 0 or random.uniform(0, 1) < math.exp(-abs(delta_E) / T):
            current = next_state

        T *= cooling_rate

        level += 1

    return current, level


def repeat_until_you_get(num_iteration):
    total = 0
    good_board = 0
    for i in range(0,num_iteration):
        problem = Problem()
        answer, level = simulated_annealing(problem)
        if answer.bad_couples == 0:
            good_board += 1
        total += level
    print("in ", (good_board / num_iteration) * 100, "% we found the answer")
    print("in average we need ", math.ceil(total/20), " levels to find the answer")


problem = Problem()
answer, level = simulated_annealing(problem)
print_answer(answer)
repeat_until_you_get(20)
