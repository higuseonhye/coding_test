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

"""
이 코드는 n개의 자연수로 이루어진 최고의 집합을 구하는 프로그램입니다.

n이 s보다 크다면 [-1]을 반환합니다.
n과 s가 같다면 1부터 n까지의 수를 원소로 갖는 리스트를 반환합니다.
n이 s보다 작다면, n개의 숫자를 구합니다. s//n으로 각 숫자를 구하고, s % n으로 나머지를 구합니다. 
이후, 나머지만큼 res 리스트의 첫 부분에 1씩 더합니다. 그리고, 오름차순으로 정렬한 뒤 반환합니다.
"""
