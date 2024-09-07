from typing import List

NUM_OF_QUEENS = 9


class CSP:
    def __init__(self, num):
        self.problem_di = num

    def is_complete_assignment(self, assignment_arg):
        for i in range(0, NUM_OF_QUEENS):
            if assignment_arg[i] == -1:
                return False
        return True


    def conflict_in_positions(self, column, assignment_arg):
        result_ls = [0] * NUM_OF_QUEENS
        for i in range(NUM_OF_QUEENS):
            if assignment_arg[i] != -1 and i != column:
                result_ls[assignment_arg[i]] += 1
                if assignment_arg[i] - abs(column - i) >= 0:
                    result_ls[assignment_arg[i] - abs(column - i)] += 1
                else:
                    if assignment_arg[i] + abs(column - i) < NUM_OF_QUEENS:
                        result_ls[assignment_arg[i] + abs(column - i)] += 1
        num_of_con = 0
        for i in range(NUM_OF_QUEENS):
            if result_ls[i] != 0:
                num_of_con += 1

        return result_ls, num_of_con


    def least_constraining_value(self, column, assignment_var):
        ls, num = self.conflict_in_positions(column, assignment_var)
        indexed_list = list(enumerate(ls))
        sorted_indexed_list = sorted(indexed_list, key=lambda x: x[1])
        original_indices = [index for index, _ in sorted_indexed_list]
        return original_indices


    def most_constrained_variable(self, assignment_arg):
        index = -1
        most_constrained = -1
        for i in range(NUM_OF_QUEENS):
            if assignment_arg[i] == -1:
                ls, num_of_con = csp.conflict_in_positions(i, assignment_arg)
                if most_constrained < num_of_con:
                    most_constrained = num_of_con
                    index = i
        return index


    def consistent(self, var, value, assignment):
        for i in range(0, NUM_OF_QUEENS):
            if assignment[i] != -1:
                if assignment[i] == value or abs(i - var) == abs(assignment[i] - value):
                    return False
        return True


    def print_board(self, result):
        for i in range(0, NUM_OF_QUEENS):
            for j in range(0, NUM_OF_QUEENS):
                if result[i] == j:
                    print("1  ", end="")
                else:
                    print("0  ", end="")
            print("\n")


def select_unassigned_variable(csp, assignment_arg):
    return csp.most_constrained_variable(assignment_arg)


def order_domain_values(csp, column, assignment_var):
    return csp.least_constraining_value(column, assignment_var)


def backtrack(csp, assignment):
    if csp.is_complete_assignment(assignment):
        return assignment
    var = select_unassigned_variable(csp, assignment)
    for value in order_domain_values(csp, var, assignment):
        if csp.consistent(var, value, assignment):
            assignment[var] = value
            result = backtrack(csp, assignment)
            if result != "failure":
                return result
            assignment[var] = -1

    return "failure"


assignment = [-1] * NUM_OF_QUEENS
csp = CSP(NUM_OF_QUEENS)
result = backtrack(csp, assignment)
if result == "failure":
    print(result)
else:
    print(result)
    csp.print_board(result)

