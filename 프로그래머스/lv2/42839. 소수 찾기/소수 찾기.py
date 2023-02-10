from itertools import permutations

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    primes = set()
    for i in range(1, len(numbers) + 1):
        perms = set(map(int, map("".join, permutations(numbers, i))))
        for perm in perms:
            if is_prime(perm):
                primes.add(perm)
    return len(primes)
