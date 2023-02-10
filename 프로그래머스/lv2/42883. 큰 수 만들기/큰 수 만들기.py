def solution(number, k):
    stack = []
    for i in range(len(number)):
        while k and stack and stack[-1] < number[i]:
            stack.pop()
            k -= 1
        stack.append(number[i])
    if k:
        stack = stack[:-k]
    return ''.join(stack)
