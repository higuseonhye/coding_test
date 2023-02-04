"""
주어진 문자열의 0의 개수를 계산하고, 문자열의 길이가 1이 될 때까지 반복하며 이진 변환을 수행합니다. 각 반복마다 이진 변환 횟수와 0의 개수를 계산하여 결과를 리턴합니다.
"""

def solution(s):
    zero_count = s.count('0')
    binary_count = 0
    while len(s) > 1:
        s = bin(len(s) - s.count('0'))[2:]
        binary_count += 1
        zero_count += s.count('0')
    return [binary_count, zero_count]
