def solution(numbers):
    answer = []
    stack = []
    for i, num in enumerate(numbers):
        while stack and stack[-1][1] < num:
            idx, val = stack.pop()
            answer[idx] = num
        stack.append((i, num))
        answer.append(-1)
    return answer

