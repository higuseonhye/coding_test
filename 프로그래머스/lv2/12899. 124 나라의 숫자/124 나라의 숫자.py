def solution(n):
    answer = ''
    nums = ['1', '2', '4']
    while n > 0:
        n -= 1
        answer = nums[n % 3] + answer
        n //= 3
    return answer
"""
This solution uses the modulo operator % and integer division // to convert the decimal number n to a ternary number represented as a string. 
The nums list stores the possible digits in the 124 country, and the answer string will store the final result.
"""
"""
Here's a line by line explanation of the code:

def solution(n): 
    - This line defines the function solution that takes an argument n.
answer = '' 
    - This line initializes the variable answer to an empty string. 
    - This string will eventually store the final answer in 124 country's numbering system.
nums = ['1', '2', '4'] 
    - This line initializes a list called nums that contains the 3 digits used in the 124 country's numbering system.
while n > 0: 
    - This line starts a while loop that will continue until n is no longer greater than 0.
n -= 1 
    - This line decrements n by 1. 
    - This is done to make the code work properly, as the numbering system used in 124 country starts from 1, but our algorithm starts from 0.
answer = nums[n % 3] + answer 
    - This line updates the answer variable. 
    - The value of nums[n % 3] is the next digit that should be added to answer in the 124 country's numbering system. 
    - The % operator is used to find the remainder when n is divided by 3, and the resulting index is used to access the corresponding digit from the nums list. 
    - The new digit is added to the front of the answer string using the concatenation operator +.
n //= 3 
    - This line updates the value of n by dividing it by 3 and discarding the remainder. 
    - This is done to move on to the next digit in the 124 country's numbering system.
return answer 
    - This line returns the final value of answer as the output of the function.

The function ends here.
"""
