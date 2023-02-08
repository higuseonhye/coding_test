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

"""
This code is a solution to a problem where given a positive integer n as the base number, 
    a positive integer t as the number of turns, 
    a positive integer m as the number of players, 
    and a positive integer p as the player's order, 
    the function returns a string that represents the order of the players to receive the information from t turns.

The change_base function takes in a number and its base, and converts the number to a string representation of that number in the specified base. 
It uses a while loop to repeatedly divide the number by the base and add the remainder to the front of the result string. 
If the remainder is 10 or higher, it is converted to a corresponding alphabet character.

The main function keeps track of a count of turns (cnt), the current number being processed (num_cnt), 
    and a list of the digits of the string representation of each number (now_num). 

It then uses two nested while loops to:
- Increment num_cnt and convert it to the string representation in the desired base (using change_base) 
    until the length of now_num is greater than or equal to the player's order p.
- Add the p-th character of now_num to the result string, and increment p by the number of players m.

The function returns the result string after t turns have been processed.
"""
