from math import gcd

def lcm(a, b):
    return a * b // gcd(a, b)

def solution(arr):
    answer = arr[0]
    for i in range(1, len(arr)):
        answer = lcm(answer, arr[i])
    return answer

"""
This code defines a function lcm which takes in two integers a and b and returns the least common multiple of the two numbers. 
The least common multiple is calculated by multiplying a and b and then dividing the result by their greatest common divisor. 
The greatest common divisor is calculated using the gcd function from the math library.

The solution function takes in a list of integers arr and returns the least common multiple of all the numbers in the list. 
It initializes a variable answer with the first element of the list, 
    and then iterates over the remaining elements, updating the value of answer at each step 
    to be the least common multiple of the current value of answer and the current element in the loop.
    
In the end, the final value of answer is returned as the solution.
"""
