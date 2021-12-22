from json import loads
from math import ceil

def process(inputs):
    f = open(inputs, "r").read().split("\n")
    lists = [loads(x) for x in f]

    return lists

class Node:
    def __init__(self, value=None):
        self.parent = None
        self.left = None
        self.right = None
        self.value = value

def tree(lists):
    root = Node()
    if isinstance(lists, int):
        root.value = lists
        return root

    root.left = tree(lists[0])
    root.right = tree(lists[1])
    root.left.parent = root
    root.right.parent = root
    reduction(root)

    return root

def add(first, second):
    root = Node()
    root.left = first
    root.right = second
    root.left.parent = root
    root.right.parent = root
    reduction(root)

    return root

def magnitude(root):
    if type(root.value) == int:
        return root.value

    return 3*magnitude(root.left) + 2*magnitude(root.right)

def reduction(root):
    done = True
    stack = [(root, 0)]
    while len(stack) > 0:
        node, depth = stack.pop()
        if node == None:
            continue

        condition = (node.left == None and node.right == None) or (node.left.value != None and node.right.value != None)
        if depth >= 4 and node.value == None and condition:
            previous = node.left
            current = node
            while current != None and (current.left == previous or current.left == None):
                previous = current
                current = current.parent

            if current != None:
                current = current.left
                while current.value == None:
                    if current.right != None:
                        current = current.right
                    else:
                        current = current.left

                current.value += node.left.value

            previous = node.right
            current = node
            while current != None and (current.right == previous or current == None):
                previous = current
                current = current.parent

            if current != None:
                current = current.right
                while current.value == None:
                    if current.left != None:
                        current = current.left
                    else:
                        current = current.right

                current.value += node.right.value

            node.value = 0
            node.left = None
            node.right = None
            done = False
            break
        
        stack.append((node.right, depth + 1))
        stack.append((node.left, depth + 1))
    
    if not done:
        reduction(root)
        return

    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        if node == None:
            continue
            
        if node.value != None:
            assert node.left == None and node.right == None
            if node.value >= 10:
                node.left = Node(node.value//2)
                node.right = Node(ceil(node.value/2))
                node.left.parent = node
                node.right.parent = node
                node.value = None

                done = False
                break
        
        stack.append(node.right)
        stack.append(node.left)

    if not done:
        reduction(root)

def sol(inputs):
    lists = process(inputs)
    root = tree(lists[0])
    lists.pop(0)
    for i in lists:
        root = add(root, tree(i))

    return magnitude(root)

def sol2(inputs):
    lists = process(inputs)
    mags = []
    for i in lists:
        for j in lists:
            mags.append(magnitude(add(tree(i), tree(j))))

    return max(mags)

def main():
    inputs = "18.txt"

    solution1 = sol(inputs)
    solution2 = sol2(inputs)

    print(f"For Puzzle 1: {solution1}")
    print(f"For Puzzle 2: {solution2}")

if __name__ == "__main__":
    main()