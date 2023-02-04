"""
주어진 문자열의 0의 개수를 계산하고, 문자열의 길이가 1이 될 때까지 반복하며 이진 변환을 수행합니다. 
각 반복마다 이진 변환 횟수와 0의 개수를 계산하여 결과를 리턴합니다.
"""
def solution(s):
    zero_count = s.count('0')
    binary_count = 0
    while len(s) > 1:
        s = bin(len(s) - s.count('0'))[2:]
        binary_count += 1
        zero_count += s.count('0')
    return [binary_count, zero_count]

"""
s = bin(len(s) - s.count('0'))[2:]

위 코드는 s 문자열의 길이에서 0의 개수를 뺀 값을 2진수 문자열로 변환한 것입니다. 

예를 들어, "110100"이라는 문자열이 주어진 경우, 
len("110100") - "110100".count('0') = 6 - 2 = 4 이므로 bin(4) = "0b100" 이고, 
[2:]를 통해 "100"이라는 문자열을 얻을 수 있습니다. 
이 값을 s 문자열에 대입하여 다음 반복에서 처리할 수 있도록 합니다.
"""

"""
bin: https://www.w3schools.com/python/ref_func_bin.asp
"""
