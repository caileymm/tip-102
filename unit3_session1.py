# standard problem set 1

# problem 1
def is_valid_post_format(posts):
    tag_dict = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    
    tag_stack = []
    
    for tag in posts:
        if tag_stack and tag in tag_dict.keys():
            if tag_stack[-1] != tag_dict[tag]: # top of stack != open tag
                return False
            else:
                tag_stack.pop()
        else:
            tag_stack.append(tag)
    
    if not tag_stack: # not empty
        return True

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))

# problem 2
def reverse_comments_queue(comments):
    stack = []
    for comment in comments:
        stack.append(comment)
    reversed = []

    while stack:
        reversed.append(stack.pop())
    return reversed

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))
print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))

# problem 3
def is_symmetrical_title(title):
    left_pointer = 0
    right_pointer = len(title) - 1
    while left_pointer < right_pointer:
        while left_pointer<right_pointer and title[left_pointer] == ' ':
            left_pointer += 1
        while left_pointer<right_pointer and title[right_pointer] == ' ':
            left_pointer -= 1
        if title[left_pointer].lower() != title[right_pointer].lower():
            return False
        left_pointer += 1
        right_pointer -= 1
    # hey u there? 
    # can u try this and lmk ...
    return True


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media"))

# problem 4
# You track your daily engagement rates as a list of integers, sorted in non-decreasing order. 
# To analyze the impact of certain strategies, you decide to square each engagement rate and 
# then sort the results in non-decreasing order.
# Given an integer array engagements sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.
def engagement_boost(engagements):
    
    squared_engagements = []
    
    for i in range(len(engagements)):
        squared_engagement = engagements[i] * engagements[i]
        squared_engagements.append((squared_engagement, i))
    
    squared_engagements.sort(reverse=True)
    
    result = [0] * len(engagements)
    position = len(engagements) - 1
    
    for square, original_index in squared_engagements:
        result[position] = square
        position -= 1
    
    return result

