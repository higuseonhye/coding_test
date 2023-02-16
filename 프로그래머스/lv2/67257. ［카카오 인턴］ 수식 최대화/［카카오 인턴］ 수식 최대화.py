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
