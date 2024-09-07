NUM_OF_QUEENS = 9

class CSP:
    def __init__(self, num):
        self.problem_di = num

    def is_complete_assignment(self, assignment_arg):
        for i in range(0, NUM_OF_QUEENS):
            if assignment_arg[i] == -1:
                return False
        return True

    def select_var_base_on_problem(self, assignment_arg):
        for i in range(0, NUM_OF_QUEENS):
            if assignment_arg[i] == -1:
                return i

    def select_val_base_on_problem(self):
        possible_domain = [-1] * NUM_OF_QUEENS
        for i in range(0, NUM_OF_QUEENS):
            possible_domain[i] = i
        return possible_domain

    def consistent(self, var, value, assignment):
        for i in range(0, NUM_OF_QUEENS):
            if assignment[i] != -1:
                if assignment[i] == value or abs(i - var) == abs(assignment[i] - value):
                    return False
        return True

def select_unassigned_variable(csp, assignment_arg):
    return csp.select_var_base_on_problem(assignment_arg)


def order_domain_values(csp):
    return csp.select_val_base_on_problem()


def backtrack(csp, assignment):
    if csp.is_complete_assignment(assignment):
        return assignment
    var = select_unassigned_variable(csp, assignment)
    for value in order_domain_values(csp):
        if csp.consistent(var, value, assignment):
            assignment[var] = value
            result = backtrack(csp, assignment)
            if result != "failure":
                return result
            assignment[var] = -1
    return "failure"

def print_board(result):
    for i in range(0, NUM_OF_QUEENS):
        for j in range(0, NUM_OF_QUEENS):
            if result[i] == j:
                print("1  ", end="")
            else:
                print("0  ", end="")
        print("\n")


csp = CSP(NUM_OF_QUEENS)
assignment = [-1] * NUM_OF_QUEENS
result = backtrack(csp, assignment)
print(result)
if result != "failure":
    print_board(result)
