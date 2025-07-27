# Set 1

# # Problem 1
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def is_circular(clues):
#     # if the linked list is empty, return false
#     if not clues:
#         return False

#     previous = []
#     current = clues.next
#     while current is not None:
#         if current == clues: # cycle with head
#             return True
#         if current in previous: # a different cycle
#             return False
#         previous.append(current)
#         current = current.next

#     return False
#     # return current.next == clues

# # Test
# # clue 1 -> clue 2 -> clue 3 -> clue 1
# clue1 = Node("The stolen goods are at an abandoned warehouse")
# clue2 = Node("The mayor is accepting bribes")
# clue3 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue1

# print(is_circular(clue1))
# # Output: True

# # Test
# # clue 1 -> clue 2 -> clue 3 -> clue 2
# clue1 = Node("The stolen goods are at an abandoned warehouse")
# clue2 = Node("The mayor is accepting bribes")
# clue3 = Node("They dumped their disguise in the lake")
# clue1.next = clue2
# clue2.next = clue3
# clue3.next = clue2

# print(is_circular(clue1))
# # Output: False

# Problem 2
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def collect_false_evidence(evidence):
    if evidence is None:
        return []
    
    collection = []
    slow = evidence
    fast = evidence
    cycle_node = None

    # just detecting a cycle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast: # there is a cycle
            cycle_node = slow.next
            break

    if cycle_node is None:
        return []

    # traverses the cycle and puts it into the list
    current = cycle_node
    print(cycle_node.value)
    while True:
        collection.append(current.value)
        current = current.next
        if current == cycle_node:
            break
    
    return collection
        

# Test
clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2

clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7

print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))
# Output:
# ['The stolen goods are at an abandoned warehouse', 'The mayor is accepting bribes', 'They dumped their disguise in the lake']
# []