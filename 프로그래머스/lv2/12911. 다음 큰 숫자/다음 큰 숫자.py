def solution(n):
    c = bin(n).count('1')
    n += 1
    while bin(n).count('1') != c:
        n += 1
    return n

