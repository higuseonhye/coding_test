def solution(order):
    stack = []
    now = 0

    for i in range(1, len(order) + 1):
        stack.append(i)

        while stack and stack[-1] == order[now]:
            now += 1
            stack.pop()

    return now
