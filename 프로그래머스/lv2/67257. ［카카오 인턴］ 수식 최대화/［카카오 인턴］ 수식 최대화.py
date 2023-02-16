import re

def solution(expression):
    # Create a list of numbers and operators from the expression
    tokens = re.findall("\d+|\D", expression)

    # Define all possible combinations of operators
    operators = ["+", "-", "*"]
    priority = [("+", "-", "*"), ("+", "*", "-"), ("-", "+", "*"), ("-", "*", "+"), ("*", "+", "-"), ("*", "-", "+")]

    # Define a function to calculate the value of an expression using a given operator
    def calculate(op, a, b):
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b

    max_value = 0
    # Iterate over all possible operator combinations and calculate the result of the expression using each combination
    for ops in priority:
        # Create copies of the list of tokens and operators to avoid modifying the original lists
        temp_tokens = tokens[:]
        temp_ops = operators[:]

        # Iterate over the current operator combination and perform calculations
        for op in ops:
            i = 0
            while i < len(temp_tokens):
                if temp_tokens[i] == op:
                    result = calculate(op, int(temp_tokens[i-1]), int(temp_tokens[i+1]))
                    temp_tokens[i-1:i+2] = [result]
                    i -= 1
                i += 1

        # The final value of the expression is the only remaining element in the list of tokens
        max_value = max(max_value, abs(temp_tokens[0]))
    return max_value

"""
This code uses regular expressions and nested loops to find the maximum possible value of an arithmetic expression containing only +, -, and * operators.

Here's a step-by-step explanation of the code:
1. The re.findall method is used to create a list of numbers and operators from the expression.
2. The list of possible operators is defined, and all possible combinations of operators are defined in the priority list.
3. The calculate function is defined to calculate the value of an expression using a given operator.
4. A variable max_value is initialized to 0 to keep track of the maximum possible value.
5. The code iterates over all possible operator combinations defined in the priority list.
6. A copy of the list of tokens and operators is created for each iteration.
7. The code iterates over the current operator combination and performs calculations on the list of tokens.
8. The final value of the expression is the only remaining element in the list of tokens. 
   The absolute value of this value is calculated and compared to the current max_value, and the larger value is assigned to max_value.
9. The function returns the final value of max_value.

In summary, the code uses regular expressions to extract the numbers and operators from the input expression, 
    and then iterates over all possible combinations of operators to calculate the maximum possible value of the expression. 
The calculate function is used to perform the arithmetic calculations.
"""
