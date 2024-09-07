# location says the current position of machine, a_state and b_state can be either clean or dirty
# corresponding to the state of right block and left block (a_state = right, b_state = left)
class State:
    def __init__(self, location, a_state, b_state):
        self.location = location
        self.a_state = a_state
        self.b_state = b_state


class Problem:
    def __init__(self, state):
        self.state = state

    def is_goal(self, state):
        if state.a_state == "clean" and state.b_state == "clean":
            return True
        return False

    # Returns all possible actions can be done in a special state
    def actions(self, state):
        action_list = []
        if state.location == "right":
            return ["left", "suck"]
        else:
            return ["right", "suck"]

    # Returns all the possible states that are result of a specific action in a specific state
    def results(self, state, action):
        result_list = []
        if action == "right":
            new_state = State("right", state.a_state, state.b_state)
            result_list.append(new_state)
        elif action == "left":
            new_state = State("left", state.a_state, state.b_state)
            result_list.append(new_state)

        # If the current block is dirty, and we want to suck, it may clean the other block or not
        # If the current block is clean, and we suck it may make that block dirty or not
        else:
            if state.location == "right" and state.a_state == "dirty":
                new_state1 = State(state.location, "clean", "clean")
                new_state2 = State(state.location, "clean", state.b_state)
                result_list.append(new_state1)
                result_list.append(new_state2)

            if state.location == "left" and state.a_state == "dirty":
                new_state3 = State(state.location, "clean", "clean")
                new_state4 = State(state.location, state.a_state, "clean")
                result_list.append(new_state3)
                result_list.append(new_state4)

            if state.location == "right" and state.a_state == "clean":
                new_state5 = State(state.location, "dirty", state.b_state)
                new_state6 = State(state.location, "clean", state.b_state)
                result_list.append(new_state5)
                result_list.append(new_state6)

            if state.location == "left" and state.a_state == "clean":
                new_state7 = State(state.location, state.a_state, "dirty")
                new_state8 = State(state.location, state.a_state, "clean")
                result_list.append(new_state7)
                result_list.append(new_state8)

        return result_list


def is_cycle(path):
    for i in range(len(path)):
        for j in range(i+1, len(path)):
            if path[i].a_state == path[j].a_state and path[i].b_state == path[j].b_state and path[i].location == path[j].location:
                return True
    return False


def print_state(state):
    print(state.location, ", ", state.a_state, ", ", state.b_state)


# In this function first we find all possible actions for the current state, then
# By and_search we find the possible states that can be result of that action
def or_search(problem, state, path):
    if problem.is_goal(state):
        return []
    if is_cycle(path):
        return "failure"

    for action in problem.actions(state):
        new_path = path + [state]
        plan = and_search(problem, problem.results(state, action), new_path)
        if plan != "failure":
            return [action] + plan

    return "failure"


# here for each state we find the proper possible action
# then we return a plan that is if else plan because there is multiple options for an action.
def and_search(problem, states, path):
    plans = []

    for s in states:
        plan_for_state = or_search(problem, s, path)
        plans.append((s, plan_for_state))

        if plan_for_state == "failure":
            return "failure"

    result_plan = []
    for state, state_plan in plans:
        work = "if " + state.location + ", " + state.a_state + ", " + state.b_state + "->"
        result_plan.extend((work, [action for action in state_plan]))

    return result_plan


def and_or_search(problem):
    return or_search(problem, problem.state, [])


st = State("right", "dirty", "dirty")
p = Problem(st)
plan = and_or_search(p)
print(plan)
