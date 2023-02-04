"""
bin(n).count('1')로 n의 2진수 표현에서 1의 개수를 계산합니다.
n을 1씩 증가시키며 2진수 표현에서 1의 개수가 c와 같아질 때 까지 반복합니다.
반복이 끝난 n을 반환합니다.
"""

def solution(n):
    c = bin(n).count('1')
    n += 1
    while bin(n).count('1') != c:
        n += 1
    return n

