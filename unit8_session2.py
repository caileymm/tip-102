from collections import deque

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
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

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

"""
Problem 1: Monstera Madness
Given the root of a binary tree where each node represents the number of splits 
in a leaf of a Monstera plant, return the number of Monstera leaves that have an 
odd number of splits.

Evaluate the time complexity of your function. Define your variables and provide 
a rationale for why you believe your solution has the stated time complexity.
"""
class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right

def count_odd_splits(root):
    if not root:
        return 0
    
    # create a stack with the number of nodes with odd values
    count = 0
    stack = [root]
    while stack:
        node = stack.pop()
        if node.val % 2 == 1:
            count += 1
        
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return count

# Test
"""
      2
     / \
    /   \
   3     5
  / \     \
 6   7     12
"""

values = [2, 3, 5, 6, 7, None, 12]
monstera = build_tree(values)

print(count_odd_splits(monstera)) # Output: 3
print(count_odd_splits(None)) # Output: 0

"""
Problem 2: Flower Finding
You are looking to buy a new flower plant for your garden. The nursery you visit stores its inventory in 
a binary search tree (BST) where each node represents a plant in the store. The plants are organized 
according to their names (vals) in alphabetical order in the BST.

Given the root of the binary search tree inventory and a target flower name, write a function find_flower() 
that returns True if the flower is present in the garden and False otherwise.

Evaluate the time complexity of your function. Define your variables and provide a rationale for why you 
believe your solution has the stated time complexity. Assume the input tree is balanced when calculating 
time complexity.
"""

class TreeNode():
     def __init__(self, value, left=None, right=None):
         self.val = value
         self.left = left
         self.right = right
         
def find_flower(inventory, name):
    if not inventory:
        return False
    
    stack = [inventory]
    while stack:
        node = stack.pop()
        if node.val == name:
            return True
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return False

# Test
"""
          Rose
         /    \
      Lilac  Tulip
      /  \       \
   Daisy Lily   Violet
"""

# using build_tree() function at top of page
values = ["Rose", "Lilac", "Tulip", "Daisy", "Lily", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  # Output: True
print(find_flower(garden, "Sunflower")) # Output: False

"""
Problem 4: Adding a New Plant to the Collection
You have just purchased a new houseplant and are excited to add it to your collection! 
Your collection is meticulously organized using a Binary Search Tree (BST) where each node 
in the tree represents a houseplant in your collection, and houseplants are organized alphabetically 
by name (val).

Given the root of your BST collection and a new houseplant name, insert a new node with value 
name into your collection. Return the root of your updated collection. If another plant with name 
already exists in the tree, add the new node in the existing node's right subtree.

Evaluate the time complexity of your function. Define your variables and provide a rationale for 
why you believe your solution has the stated time complexity. Assume the input tree is balanced when 
calculating time complexity.
"""
class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def add_plant(collection, name):
    if not collection:
        return TreeNode(name)
    
    node = collection
    while node:
        if name < node.val:
            if node.left:
                node = node.left
            else:
                node.left = TreeNode(name)
                break
        if name > node.val:
            if node.right:
                node = node.right
            else:
                node.right = TreeNode(name)
                break
    
    return collection

# Test
"""
            Money Tree
        /              \
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))
