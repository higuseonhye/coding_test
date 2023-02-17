def solution(order):
    stack = []
    now = 0

    for i in range(1, len(order) + 1):
        stack.append(i)

        while stack and stack[-1] == order[now]:
            now += 1
            stack.pop()

    return now

"""
def solution(order):
    # Initialize an empty stack and a variable to keep track of the current index in the order list
    stack = []
    now = 0

    # Iterate through the integers from 1 to the length of the order list + 1
    for i in range(1, len(order) + 1):
        # Push the current integer onto the stack
        stack.append(i)

        # While the stack is not empty and the top element of the stack matches the current element of the order list
        while stack and stack[-1] == order[now]:
            # Increment the index in the order list and pop the top element off the stack
            now += 1
            stack.pop()

    # Return the number of elements in the order list that have been matched
    return now

I hope this helps! Let me know if you have any questions.
"""
