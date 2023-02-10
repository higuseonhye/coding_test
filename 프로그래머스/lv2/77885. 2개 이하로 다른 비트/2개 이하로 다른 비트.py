# 2진수 변환
def dec_to_bin(n):
    if n == 0:
        return '0'
    bin = ''
    while n // 2 > 0:
        bin = str(n % 2) + bin
        n = n // 2
        
    return "1" + bin

# 10진수 변환
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