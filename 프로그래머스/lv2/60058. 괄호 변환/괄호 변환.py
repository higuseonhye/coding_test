def is_valid(s):
    # Initialize a stack with a value of 0
    stack = 0
    # Iterate through each character in the string
    for i in s:
        # If the character is an opening parenthesis, increment the stack
        if i == '(':
            stack += 1
        # If the character is a closing parenthesis, decrement the stack
        else:
            stack -= 1
        # If the stack becomes negative, return False
        if stack < 0:
            return False
    # Return True if the stack is 0 (indicating that the parentheses are balanced)
    return True

def reverse(s):
    # Initialize an empty string to store the reversed string
    ans = ''
    # Iterate through each character in the string
    for i in s:
        # If the character is an opening parenthesis, add a closing parenthesis to the answer string
        if i == '(':
            ans += ')'
        # If the character is a closing parenthesis, add an opening parenthesis to the answer string
        else:
            ans += '('
    # Return the reversed string
    return ans

def solution(p):
    # If the input string is empty, return an empty string
    if p == '':         
        return ''
    
    # Initialize a stack with a value of 0
    stack = 0         
    # Iterate through each character in the string
    for i in range(len(p)):
        # If the character is an opening parenthesis, increment the stack
        if p[i] == '(':
            stack += 1
        # If the character is a closing parenthesis, decrement the stack
        else:
            stack -= 1
        # If the stack becomes 0, split the string into two parts: "u" and "v"
        if stack == 0:
            u = p[:i+1]
            v = p[i+1:]
            break
            
    # If "u" is a balanced string of parentheses, return "u" concatenated with the solution to "v"
    if is_valid(u):         
        return u + solution(v)     
    # If "u" is not a balanced string of parentheses, return a balanced string by first wrapping "v" with a pair of balanced parentheses, then reversing the characters in "u" (but excluding the first and last characters, which are the balanced parentheses)
    else:        
        return '(' + solution(v) + ')' + reverse(u[1:-1])

    
"""
This is a python function that solves the "Balanced Parenthesis" problem. 
The function takes a string of parentheses as an argument and returns a balanced string of parentheses.

The function uses a stack to keep track of the balance of parentheses in the string. 
If a '(' is encountered, it pushes it onto the stack, and if a ')' is encountered, it pops the stack. 
If at any point, the stack becomes negative, it means that there is a closing parenthesis without a corresponding opening parenthesis, 
    and so the function returns False.

The function also uses a recursive approach to balance the parentheses. 
It splits the input string into two parts, "u" and "v", where "u" is the longest balanced prefix of the input string and "v" is the rest of the string. 
If "u" is already balanced, the function returns "u" concatenated with the solution to "v". 
If "u" is not balanced, the function returns a balanced string by first wrapping "v" with a pair of balanced parentheses, 
    then reversing the characters in "u" (but excluding the first and last characters, which are the balanced parentheses).
"""
