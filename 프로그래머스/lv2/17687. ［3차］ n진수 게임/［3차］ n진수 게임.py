def solution(n, t, m, p):
    alphabets = ['A', 'B', 'C', 'D', 'E', 'F']
    
    def change_base(num, base):
        result = ''
        while num >= base:
            digit = num % base
            result = (alphabets[digit - 10] if digit >= 10 else str(digit)) + result
            num //= base
        result = (alphabets[num - 10] if num >= 10 else str(num)) + result
        return result
    
    cnt = 0
    num_cnt = 0
    now_num = []
    result = ''
    while cnt < t:
        cnt += 1
        while len(now_num) < p:
            now_num.extend(list(change_base(num_cnt, n)))
            num_cnt += 1
        result += now_num[p - 1]
        p += m
    return result
