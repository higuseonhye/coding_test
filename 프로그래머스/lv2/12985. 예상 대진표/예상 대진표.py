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