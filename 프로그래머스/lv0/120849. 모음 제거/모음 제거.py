def solution(my_string):
    vowels = 'aeiou'
    return ''.join(ch for ch in my_string if ch not in vowels)


