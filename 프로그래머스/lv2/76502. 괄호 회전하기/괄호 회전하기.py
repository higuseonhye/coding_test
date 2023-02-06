def solution(s):
    n = len(s)
    if n & 1:
        return 0

    from collections import deque
    q = deque(s)

    opens = {"{", "[", "("}
    closes = {"}": "{", "]": "[", ")": "("}

    def is_valid_p(q):
        dq = deque()
        for char in q:
            if dq and char in closes and closes[char] == dq[-1]:
                dq.pop()
            elif char in closes:
                return False
            else:
                dq.append(char)
        return not dq

    if not (q[0] in opens and is_valid_p(q)):
        for i in range(n-1):
            q.rotate(-1)
            if q[0] in opens and is_valid_p(q):
                break
        else:
            return 0

    dq = deque()
    cnt = 0
    for char in q:
        if dq and char in closes and closes[char] == dq[-1]:
            dq.pop()
        else:
            dq.append(char)
        if not dq:
            cnt += 1

    return cnt
