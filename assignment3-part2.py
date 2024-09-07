from random import randint

NUM_OF_QUEENS = 9
MAX_STEP = 100

class QUEEN:
    def __init__(self):
        self.row = -1
        self.conflict = 0

class CSP:
    def __init__(self, num):
        self.csp_di = num


    def compute_conflict(self, state):
        for i in range(0, NUM_OF_QUEENS):
            state[i].conflict = 0
        for i in range(0, NUM_OF_QUEENS):
            for j in range(0, NUM_OF_QUEENS):
                if i != j:
                    if state[i].row == state[j].row or abs(i - j) == abs(state[i].row - state[j].row):
                        state[i].conflict += 1

    def initial_step(self):
        position = [QUEEN() for _ in range(0, NUM_OF_QUEENS)]
        for i in range(0, NUM_OF_QUEENS):
            position[i].row = randint(0, NUM_OF_QUEENS-1)
            position[i].conflict = 0
        self.compute_conflict(position)
        return position


    def is_solution(self, state):
        for i in range(0, NUM_OF_QUEENS):
            for j in range(i+1, NUM_OF_QUEENS):
                if state[i].row == state[j].row or abs(i-j) == abs(state[i].row-state[j].row):
                    return False
        return True


    def conflicted_variable(self, current):
        while True:
            i = randint(0, NUM_OF_QUEENS-1)
            if current[i].conflict != 0:
                return i


    def find_value(self, state, variable):
        ls = [0] * NUM_OF_QUEENS
        ls[state[variable].row] = state[variable].conflict
        min_value = state[variable].conflict
        min_index = state[variable].row
        for i in range(0, NUM_OF_QUEENS):
            for j in range(0, NUM_OF_QUEENS):
                if variable != j:
                    if i == state[j].row or abs(variable-j) == abs(i-state[j].row):
                        ls[i] += 1
            if ls[i] < min_value:
                min_value = ls[i]
                min_index = i
        return min_index, min_value


def min_conflict(csp, max_steps):
    current = csp.initial_step()
    for i in range(max_steps):
        if csp.is_solution(current):
            return current
        var = csp.conflicted_variable(current)
        current[var].row, current[var].conflict = csp.find_value(current, var)
        csp.compute_conflict(current)

    return "failure"


def print_helper(result):
    for i in range(0, NUM_OF_QUEENS):
        print(result[i].row, end=",")
    print("\n")

    for i in range(0, NUM_OF_QUEENS):
        for j in range(0, NUM_OF_QUEENS):
            if result[i].row == j:
                print("1  ", end="")
            else:
                print("0  ", end="")
        print("\n")


csp = CSP(NUM_OF_QUEENS)
result = min_conflict(csp, MAX_STEP)
if result == "failure":
    print(result)
else:
    print_helper(result)

