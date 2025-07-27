# Set 1
from collections import deque

# Tree Node class
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

# Problem 1
root = TreeNode("Trunk")

Mcintosh = TreeNode("Mcintosh")
Granny_Smith = TreeNode("Granny Smith")
Fuji = TreeNode("Fuji")
Opal = TreeNode("Crab")
Crab = TreeNode("Crab")
Gala = TreeNode("Gala")
root.left = Mcintosh
root.right = Granny_Smith
Mcintosh.left = Fuji
Mcintosh.right = Opal
Granny_Smith.left = Crab
Granny_Smith.right = Gala

# Test
# print_tree(root)

# Problem 2
def calculate_yield(root):
    operator = root.val
    left_num = root.left.val
    right_num = root.right.val
    if operator == "+":
        return left_num + right_num
    elif operator == "-":
        return left_num - right_num
    elif operator == "*":
        return left_num * right_num
    else:
        return left_num / right_num
  
apple_tree = TreeNode("+", TreeNode(7), TreeNode(5))

# Test
# print(calculate_yield(apple_tree))

# Problem 3
'''
def right_vine(root):
    output = []
    node = root
    while node:
        output.append(node.val)
        node = node.right
    return output

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# Test
# print(right_vine(ivy1))
# print(right_vine(ivy2))
'''

# Problem 4
def right_vine(root):
    if not root:
        return []

    return [root.val] + right_vine(root.right)

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

# Test
# print(right_vine(ivy1))
# print(right_vine(ivy2))
