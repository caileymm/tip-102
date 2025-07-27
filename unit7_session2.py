# def find_cruise_length(cruise_lengths, vacation_length):
#     def binary_search(arr, target, left, right):   
#         middle = (left + right) // 2
#         if left > right:
#             return False
#         if cruise_lengths[middle] == vacation_length:
#             return True
#         elif cruise_lengths[middle] < vacation_length:
#             return binary_search(cruise_lengths, vacation_length, middle + 1, right)
#         else: 
#             return binary_search(cruise_lengths, vacation_length, left, middle - 1)
#     return binary_search(cruise_lengths, vacation_length, 0, len(cruise_lengths)-1)


# print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))

# print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))

def find_cabin_index(cabins, preferred_deck):
    def binary_search(arr, target, left, right):   
        middle = (left + right) // 2
        if left > right:
            return left
        if cabins[middle] == preferred_deck:
            return middle
        elif cabins[middle] < preferred_deck:
            return binary_search(cabins, preferred_deck, middle + 1, right)
        else: 
            return binary_search(cabins, preferred_deck, left, middle - 1)
    return binary_search(cabins, preferred_deck, 0, len(cabins)-1)

#print(find_cabin_index([1, 3, 5, 6], 5))
#print(find_cabin_index([1, 3, 5, 6], 2))
#print(find_cabin_index([1, 3, 5, 6], 7))

# def count_checked_in_passengers(rooms):
#     def binary_search(arr, target, left, right):
#         middle = (left + right) // 2
#         if left > right:
#             return left
#         if rooms[middle] == 1:
#             return middle
#         elif rooms[middle] < 1:
#             return binary_search(rooms, 1, middle + 1, right)
#         else: 
#             return binary_search(rooms, 1, left, middle - 1)
#     firstOccurenceOf1 = binary_search(rooms, 1, 0, len(rooms)-1)
#     return len(rooms) - firstOccurenceOf1

# rooms1 = [0, 0, 0, 1, 1, 1, 1]
# rooms2 = [0, 0, 0, 0, 0, 1]
# rooms3 = [0, 0, 0, 0, 0, 0]

#print(count_checked_in_passengers(rooms1)) 
#print(count_checked_in_passengers(rooms2))
#print(count_checked_in_passengers(rooms3))


#Find a number x such that exactly x excursions have at least x passengers.
'''
def is_profitable(excursion_counts):
    def binary_search(arr, target, left, right):
        middle = (left+right)//2
        if left > right:
            return left
        if excursion_counts[middle] == 1:
            return middle
        elif excursion_counts[middle] < 1:
            return binary_search(excursion_counts, target, middle + 1, right)
        else: 
            return binary_search(excursion_counts, 1, left, middle - 1)
    for x in range(1, len(excursion_counts)+1):
        index = binary_search(excursion_counts, x, 0, len(excursion_counts))
        count = len(excursion_counts)+1 - index
        if count == x:
            return x
    return -1
        
print(is_profitable([3, 5]))
print(is_profitable([0, 0]))
'''
def is_profitable(excursion_counts):
    n = len(excursion_counts)
    for x in range(1, n + 1): # x is the target
        left, right = 0, n - 1
        index = n
        while left <= right:
            middle = (left + right) // 2
            if excursion_counts[middle] >= x:
                index = middle
                right = middle - 1
            else:
                left = middle + 1
        count = n - index
        if count == x:
            return x
    return -1

def is_profitable_recursive(excursion_counts):
    n = len(excursion_counts)
    def binary_search(x, left, right):
        if left > right:
            return left
        middle = (left + right) // 2
        if excursion_counts[middle] >= x:
            return binary_search(x, left, middle - 1)
        else:
            return binary_search(x, middle + 1, right)

    for x in range(1, n + 1):
        idx = binary_search(x, 0, n - 1)
        count = n - idx
        if count == x:
            return x
    return -1

print(is_profitable([3, 5]))
print(is_profitable([0, 0]))

print(is_profitable_recursive([3, 5]))
print(is_profitable_recursive([0, 0]))