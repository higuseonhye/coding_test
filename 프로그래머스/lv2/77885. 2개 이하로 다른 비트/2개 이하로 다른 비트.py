def dec_to_bin(n):
    if n == 0:
        return '0'
    bin = ''
    while n // 2 > 0:
        bin = str(n % 2) + bin
        n = n // 2
        
    return "1" + bin

def bin_to_dec(bin):
    digit = 1
    dec = 0
    for s in reversed(bin):
        if s == '1':
            dec += digit
        digit *= 2
    
    return dec
     
def solution(numbers):
    answer = []

    for number in numbers:
        bin = "0" + dec_to_bin(number)

        if bin == '00':
            answer.append(1)
            continue
        
        if bin[-1] == '0':
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
