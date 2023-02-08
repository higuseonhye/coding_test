def solution(n, t, m, p):
    def change_binary(number):
        result = ''
        if number == 0 :
            return str(0)
        while number >= n:
            result = str(number % n) + result
            number //= n            
        result = str(number % n) + result
        return result

    def turn_alphabet(number):
        alphabets = ['A', 'B', 'C', 'D', 'E', 'F']
        if 10 <= number < n :
            return alphabets[number % 10]        
        if number >= 10:
            number %= 10
            return alphabets[number]
        else :
            return str(number)

    def change_heximal(number):
        result = ''
        if number < n :
            return turn_alphabet(number)
        while number >= n:
            result = turn_alphabet(number % n) + result
            number //= n
        result = turn_alphabet(number % n) + result
        return result

    cnt = 0
    now_num = []
    result = ''
    if n <= 10:
        num_cnt = 0
        while cnt < t :
            cnt += 1
            while len(now_num) < p :                
                now_num.extend(list(change_binary(num_cnt)))
                num_cnt += 1
                if len(now_num) >= p:
                    break
            result += now_num[p - 1]
            p += m
    else :
        num_cnt = 0
        while cnt < t :
            cnt += 1
            while len(now_num) < p :
                now_num.extend(list(change_heximal(num_cnt)))
                num_cnt += 1
            result += now_num[p - 1]
            p += m
    return result
