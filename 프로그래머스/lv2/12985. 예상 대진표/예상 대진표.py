def find_rank(n, a, b):
    exp_a = next((i for i in range(n) if 2**i >= a), n)
    exp_b = next((i for i in range(exp_a, n) if 2**i >= b), n)
    if exp_a == exp_b:
        num = 2**(exp_a-1)
        return find_rank(n-num, a-num, b-num)
    else:
        return exp_b

def solution(n, a, b):
    if a > b:
        a, b = b, a
    return find_rank(n, a, b)

"""
The find_rank function takes three arguments: n, a, and b. 
It calculates the largest power of 2 that is less than or equal to a, represented by exp_a, 
    and the largest power of 2 that is less than or equal to b, represented by exp_b. 
If exp_a and exp_b are equal, the function recursively calls itself with updated arguments n-num, a-num, and b-num (where num is equal to 2^(exp_a-1)). 
If exp_a is not equal to exp_b, the function returns exp_b.

The solution function takes three arguments: n, a, and b. If a is greater than b, it swaps their values. 
Then, it calls the find_rank function with n, a, and b as arguments and returns the result.

The code returns the rank of the smallest power of 2 that is greater than or equal to the maximum of a and b within the first n positive integers.
"""
