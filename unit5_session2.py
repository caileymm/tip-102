# Set 1

# Problem 1
# class Villager:
#     def __init__(self, name, species, catchphrase):
#         self.name = name
#         self.species = species
#         self.catchphrase = catchphrase
#         self.friends = []

#     def get_mutuals(self, new_contact):
#         # for each of this person's friends compare to new_contact's friends
#         # if there is a similarity, then add friend to a list
#         # return the list

#         mutual_friends = []

#         if not self.friends:
#             return []

#         for friend in self.friends:
#             if friend in new_contact.friends:
#                 mutual_friends.append(friend.name)

#         return mutual_friends
    
# # Tests
# bob = Villager("Bob", "Cat", "pthhhpth")
# marshal = Villager("Marshal", "Squirrel", "sulky")
# ankha = Villager("Ankha", "Cat", "me meow")
# fauna = Villager("Fauna", "Deer", "dearie")
# raymond = Villager("Raymond", "Cat", "crisp")
# stitches = Villager("Stitches", "Cub", "stuffin")

# bob.friends = [stitches, raymond, fauna]
# marshal.friends = [raymond, ankha, fauna]
# print(bob.get_mutuals(marshal))

# ankha.friends = [marshal]
# print(bob.get_mutuals(ankha))


# Problem 2
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# kk_slider.next = harriet
# harriet.next = saharah
# saharah.next = isabelle

# # Test
# print_linked_list(kk_slider) # Output: K.K. Slider -> Harriet -> Saharah -> Isabelle

# # Problem 3
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def add_first(head, task):
#     #
#     new_node = Node(task)
#     if head is not None:
#         new_node.next = head
#     head = new_node
#     return new_node

# # Test
# task_1 = Node("shake tree")
# task_2 = Node("dig fossils")
# task_3 = Node("catch bugs")
# task_1.next = task_2
# task_2.next = task_3

# # Linked List: shake tree -> dig fossils -> catch bugs
# print_linked_list(add_first(task_1, "check turnip prices"))

# # Problem 4
# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def halve_list(head):
#     # traverse linked list (start from head node, change self.value to half, go to self.next node)
    
#     if head is None:
#         return head

#     current = head
#     while current is not None:
#         current.value = current.value / 2 
#         current = current.next
    
#     return head

# # Test
# node_one = Node(5)
# node_two = Node(6)
# node_three = Node(7)
# node_one.next = node_two
# node_two.next = node_three

# # Input List: 5 -> 6 -> 7
# print_linked_list(halve_list(node_one))

# Problem 5
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def delete_tail(head):
    if head is None:
        return head
    
    previous = head
    current = head
    while current is not None:
        if current.next is None:
            previous.next = None
        # the problem was the order of assigning previous and current
        previous = current
        current = current.next
    
    return head

butterfly = Node("Common Butterfly")
ladybug = Node("Ladybug")
beetle = Node("Scarab Beetle")
butterfly.next = ladybug
ladybug.next = beetle

# Input List: butterfly -> ladybug -> beetle
print_linked_list(delete_tail(butterfly))
