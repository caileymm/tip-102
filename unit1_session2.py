# set 1

# problem 1
# def reverse_sentence(sentence):
#     # Understand:
#     # Reverse words in the string, not entire string
#     # Edge case - if only one word - return original string
#     # Words are separated by spaces
#     # Plan 1 - separate sentence into multiple word strings, store word strings in list,
#     # create new string by going through the list in reverse order
#     words = sentence.split()
#     words_len = len(words)
#     return_str = ""
#     # for i in range(words_len)
#     for i in range(words_len - 1, -1, -1):
#         return_str += words[i]
#         if i != 0:
#             return_str += " "
#     return return_str

# sentence = "tubby little cubby all stuffed with fluff"
# print(reverse_sentence(sentence))
# sentence = "Pooh"
# print(reverse_sentence(sentence))

# problem 2
def goldilocks_approved(nums):
    # Understanding
    # Input is list of positive unique integers
    # Return any number that is not max or min value
    # Plan 1 - keep track of max, min values
    # Plan 2 - find max, min values, then return first non-matching value
    max_val = max(nums)
    min_val = min(nums)
    for i in range(len(nums)):
        cur_num = nums[i]
        if cur_num != max_val and cur_num != min_val:
            return cur_num
    return -1

# nums = [3, 2, 1, 4]
# print(goldilocks_approved(nums)) #Expected = 3
# nums = [1, 2]
# print(goldilocks_approved(nums)) # Expected = -1
# nums = [2, 1, 3]
# print(goldilocks_approved(nums)) # Expected = 2

# problem 3
def delete_minimum_elements(hunny_jar_sizes):
    # Understanding
    # Continously remove minimum element until list is empty
    # Return a new list of elements in the order in which they removed
    # Plan 1 - remove min element, update original list, keep removing min element of shrinking original list - append to new list as we go
    new_list = []
    while len(hunny_jar_sizes) > 0:
        # find min element
        min_element = min(hunny_jar_sizes)
        # remove
        hunny_jar_sizes.remove(min_element)
        # add removed element to new list
        new_list.append(min_element)
    return new_list

# hunny_jar_sizes = [5, 3, 2, 4, 1]
# print(delete_minimum_elements(hunny_jar_sizes)) # Expected: [1, 2, 3, 4, 5]
# hunny_jar_sizes = [5, 2, 1, 8, 2]
# print(delete_minimum_elements(hunny_jar_sizes)) # Expected : [1, 2, 2, 5, 8]

# problem 4
def sum_of_digits(num):
    # sum of digits within num
    # Plan 1 - use mod to get individual digit to add for the sum
    # Use integer division to reduce original number so that mod results in single digits remainders
    sum = 0
    while num != 0:
        sum += num % 10
        num = int(num / 10)
    return sum

num = 423
print(sum_of_digits(num))
num = 4
print(sum_of_digits(num))