def solution(n, left, right):
    results = []
    for x in range(left, right+1):
        results.append(max(divmod(x, n)) + 1)
    return results


