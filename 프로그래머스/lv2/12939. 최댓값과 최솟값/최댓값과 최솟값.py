def solution(s):
    _s = list(map(int, s.split()))
    return str(min(_s)) + " " + str(max(_s))
