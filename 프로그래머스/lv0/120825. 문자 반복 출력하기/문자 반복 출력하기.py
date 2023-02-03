"""
n만큼 반복한 문자열 return -> ''.join
"""
def solution(my_string, n):
    return ''.join(i*n for i in my_string)