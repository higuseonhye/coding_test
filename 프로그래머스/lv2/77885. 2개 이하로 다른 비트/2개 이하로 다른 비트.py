def dec_to_bin(n):
    # 10진수를 2진수로 변환하는 함수
    if n == 0:
        # n이 0이면 '0'을 반환
        return '0'
    bin = ''
    # bin에 2진수를 저장할 빈 문자열
    while n // 2 > 0:
        # n이 2로 나누어질 때 까지 반복
        bin = str(n % 2) + bin
        # bin에 n을 2로 나눈 나머지를 추가
        n = n // 2
        # n을 2로 나눈 몫을 n에 저장
        
    return "1" + bin
    # bin에 1을 추가하여 반환

def bin_to_dec(bin):
    # 2진수를 10진수로 변환하는 함수
    digit = 1
    dec = 0
    # dec에 10진수를 저장할 변수
    for s in reversed(bin):
        # bin의 맨 뒤부터 각 자리수에 대해 반복
        if s == '1':
            dec += digit
            # s가 '1'이면 dec에 digit을 더함
        digit *= 2
        # digit을 2로 곱함
    
    return dec
    # dec를 반환
     
def solution(numbers):
    answer = []
    # answer에 답을 저장할 빈 리스트

    for number in numbers:
        bin = "0" + dec_to_bin(number)
        # bin에 number를 2진수로 변환한 값을 저장

        if bin == '00':
            # bin이 '00'이면
            answer.append(1)
            # answer에 1을 추가
            continue
        
        if bin[-1] == '0':
            # bin의 마지막 자리가 '0'이면
            answer.append(bin_to_dec(bin[:len(bin)-1]+'1'))
            continue

        new_bin = ''
        for s in reversed(range(1, len(bin))):
            if bin[s-1:s+1] == "01":
                new_bin = bin[:s-1] + "10" + bin[s+1:]
                break
        
        answer.append(bin_to_dec(new_bin))
                          
    return answer

"""
이 코드는 solution 함수를 통해서 10진수 리스트를 받아 각 숫자들의 가장 작은 2진수로의 변환을 수행한 결과를 리스트 형태로 반환하는 코드입니다.
- dec_to_bin 함수는 10진수 숫자를 2진수 문자열로 변환하는 함수이며, 
- bin_to_dec 함수는 2진수 문자열을 10진수 숫자로 변환하는 함수입니다. 
- solution 함수는 입력받은 10진수 리스트를 각각 2진수 문자열로 변환한 뒤, 
    각 2진수 문자열의 마지막 비트가 0인 경우와 1인 경우에 따라서 새로운 2진수 문자열을 생성하고, 이를 10진수로 변환하여 반환합니다.
"""
"""
