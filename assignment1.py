class Node:
    def __init__(self, X, Y, A, B, G, PL):
        self.A_capacity = X
        self.B_capacity = Y
        self.A_water = A
        self.B_water = B
        self.Cost = G
        self.parent = []
        self.parent.extend(PL)
        self.parent.append(A)
        self.parent.append(B)
def is_goal(node, a, b):
    if (node.A_water is a and node.B_water is b):
        return True
    return False

def empty(node):
    node1 = Node(node.A_capacity, node.B_capacity, 0, node.B_water, node.Cost + 1, node.parent)
    node2 = Node(node.A_capacity, node.B_capacity, node.A_water, 0, node.Cost + 1, node.parent)
    return [node1, node2]

def full(node):
    node1 = Node(node.A_capacity, node.B_capacity, node.A_capacity, node.B_water, node.Cost + 1, node.parent)
    node2 = Node(node.A_capacity, node.B_capacity, node.A_water, node.B_capacity, node.Cost + 1, node.parent)
    return [node1, node2]

def pour(node):
    # pouring A into B
    if node.A_water <= (node.B_capacity - node.B_water): # pour until A becomes empty
        node1 = Node(node.A_capacity, node.B_capacity, 0, node.B_water + node.A_water, node.Cost + 1, node.parent)
    else: # pour until B becomes full
        node1 = Node(node.A_capacity, node.B_capacity, node.A_water-(node.B_capacity - node.B_water), node.B_capacity, node.Cost + 1, node.parent)

    # pouring B into A
    if node.B_water <= (node.A_capacity - node.A_water): # pour until B becomes empty
        node2 = Node(node.A_capacity, node.B_capacity, node.A_water + node.B_water, 0, node.Cost + 1, node.parent)
    else: # pour until A becomes full
        node2 = Node(node.A_capacity, node.B_capacity, node.A_capacity, node.B_water-(node.A_capacity - node.A_water), node.Cost + 1, node.parent)

    return [node1, node2]
def Expand(node):
    result = []
    result.extend(empty(node))
    result.extend(full(node))
    result.extend(pour(node))
    return result

def cout(child):
    print(child.A_capacity, child.B_capacity, child.A_water, child.B_water, child.Cost, print(child.parent))
def BFS(X, Y, a,b ):

    root_node = Node(X, Y, 0, 0, 0, [])
    if is_goal(root_node, a, b):
        return root_node
    frontier = [root_node]
    reached = [[0,0]]

    while frontier :
        node = frontier.pop(0)
        for child in Expand(node):
            if is_goal(child, a, b):
                return child
            l = [child.A_water,child.B_water]
            if l not in reached:
                reached.append([child.A_water,child.B_water])
                frontier.append(child)

    return None
node = BFS(10,3, 10,1)
i = 0
if node != None:
    while i < len(node.parent):
        print(node.parent[i], node.parent[i+1])
        i += 2
else:
    print("failure")

print("#-------------------------  ITERATIVE-DEEPENING-SEARCH -------------------------#")

def DLS(X, Y, a, b, l):
    root_node = Node(X, Y, 0, 0, 0, [])
    frontier = [root_node]
    reached = [[0,0]]
    result = "failure"
    while frontier:
        node = frontier.pop(0)
        if is_goal(node, a, b):
            return node
        if node.Cost >= l-1:
            result = "cutoff"
        else:
            # print(node.A_water,node.B_water)
            for child in Expand(node):
                li = [child.A_water, child.B_water]
                if li not in reached:
                    reached.append([child.A_water, child.B_water])
                    frontier.insert(0,child)

    return result

def IDS(X, Y, a, b):
    l = 0
    while True:
        if DLS(X,Y, a, b,l) != "cutoff":
            return DLS(X,Y, a, b,l)
        else:
            l += 1
node = IDS(10,3, 10, 1)
i = 0
if node == "failure" :
    print(node)
else:
    while i < len(node.parent):
        print(node.parent[i], node.parent[i+1])
        i += 2


