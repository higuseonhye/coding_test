def solution(number, k):
    stack = []
    for i in range(len(number)):
        while k and stack and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    if k:
        stack = stack[:-k]
    return ''.join(stack)

"""
Overall, this code implements a greedy algorithm. 
We loop through the digits of the input number and remove the smaller digits first, 
    until we reach the desired length or we can no longer remove any more elements.
The result is the largest number we can get.
"""
"""
Let's go through the code line by line:

stack = []: 
    - We initialize an empty list stack to store the final number we want to get.
for i in range(len(number)):: 
    - We loop through the input number and get each digit.
while k and stack and stack[-1] < number[i]:: 
    - We keep popping the elements from the stack until we can no longer remove any elements or k is 0. The elements we pop are those that are smaller than the current digit, number[i]. This is because we want to get the largest possible number, so we want to remove the smaller digits first.
stack.append(number[i]): 
    - We append the current digit to the stack.
if k:: 
    - If k is still greater than 0, we remove the last k elements from the stack as they are the smallest elements.
return ''.join(stack): 
    - We return the stack as a string by joining its elements.
"""
