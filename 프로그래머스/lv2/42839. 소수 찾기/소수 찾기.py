# Import the permutations function from the itertools module
from itertools import permutations

# Define a function to check if a number is prime
def is_prime(n):
    # Return False for numbers less than 2, as they are not prime
    if n < 2:
        return False
    # Loop through numbers from 2 to the square root of n, inclusive
    for i in range(2, int(n**0.5) + 1):
        # If n is divisible by i, it is not prime, 
        if n % i == 0:
            return False
    # If the loop ends, n is prime
    return True

# Define the main solution function
def solution(numbers):
    # Convert the numbers string to a list
    numbers = list(numbers)
    # Initialize a set to store the prime numbers found
    primes = set()
    # Loop through the length of the numbers list, from 1 to the length of the list, inclusive
    for i in range(1, len(numbers) + 1):
        # Get all possible permutations of length i using the permutations function
        perms = set(map(int, map("".join, permutations(numbers, i))))
        # Loop through each permutation
        for perm in perms:
            # If the permutation is prime, add it to the set of primes
            if is_prime(perm):
                primes.add(perm)
    # Return the number of primes found
    return len(primes)


"""
This code uses the itertools module to generate all possible permutations of the numbers in the input string, 
    and then uses the is_prime function to check if each permutation is a prime number. 
The primes are stored in a set to ensure that duplicates are not counted. Finally, the length of the set is returned as the answer.
"""
