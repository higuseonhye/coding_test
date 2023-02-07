def solution(n, s):
    if n > s:
        return [-1]
    elif n == s:
        return [i for i in range(1, n+1)]
    else:
        res = [s//n] * n
        rest = s % n
        for i in range(rest):
            res[i] += 1
        return sorted(res)
