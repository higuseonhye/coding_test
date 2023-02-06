def solution(n):
    count = 0
    while n != 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
            count += 1
    return count

"""
This function implements a simple algorithm for counting the number of operations needed to make a number 0. The algorithm works as follows:

1. Check if the number is divisible by 2. If it is, divide the number by 2.
2. If the number is not divisible by 2, subtract 1 from the number and increment the count by 1.
3. Repeat the process until the number becomes 0.
4. Return the count.
"""
