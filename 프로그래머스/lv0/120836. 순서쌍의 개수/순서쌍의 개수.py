"""
두 숫자의 곱이 n인 자연수 순서쌍의 개수 -> 나누기 나머지 0
계수 -> len
"""
def solution(n): 
    return len([i for i in range(1, n+1) if n % i == 0])