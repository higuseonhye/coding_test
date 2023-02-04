"""
It uses a stack data structure to store the characters in the string, and for each character it checks if the last character in the stack is the same. 
If it is, then the last character is popped from the stack. 
If not, then the current character is pushed onto the stack. 
Finally, if the stack is empty, then the function returns 1 as the string has been completely removed. 
If the stack is not empty, then the function returns 0 as some characters were unable to be removed.

At the end, if the stack is empty, it means all pairs have been successfully removed and the function returns 1, 
    otherwise, it returns 0, indicating that the removal was not successful.
"""
def solution(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return 1 if not stack else 0
