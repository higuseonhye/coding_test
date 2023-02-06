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


"""
The given code defines a function called solution which takes a string s 
    as input and returns the count of balanced sub-strings in the string.

The code first checks if the length of the input string s is even. 
If it is odd, then the function returns 0 because an odd-length string cannot contain balanced sub-strings.

The code then creates a double-ended queue q from the input string s. 
It then defines a set opens of opening brackets and a dictionary closes 
    that maps closing brackets to their corresponding opening bracket.

The code then defines an inner function is_valid_p which takes a double-ended queue q 
    as input and returns True if the given queue represents a balanced string (using a stack-like approach).

The code then checks if the first bracket in the q is an opening bracket and the queue represents a valid balanced string. 
If it does not, the code rotates the queue to the left and repeats the same check until a valid balanced string is found. 
If no valid balanced string is found, the function returns 0.

Finally, the code iterates through the queue, updating a double-ended queue dq to maintain the current balanced status. 
If the current bracket is a closing bracket that matches the last opening bracket in dq, 
    the code pops the last opening bracket from dq. 
Otherwise, the code adds the current bracket to dq. 
If dq becomes empty, the code increments the count of balanced sub-strings. 
The final result is returned by the function.
"""
