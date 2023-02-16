def solution(topping):
    answer = 0
    forward = set()
    backward = {}
    for i in topping:
        backward[i] = backward.get(i, 0) + 1
    for i in topping:
        forward.add(i)
        backward[i] -= 1
        if backward[i] == 0:
            del backward[i]
        if len(forward) == len(backward):
            answer += 1
    return answer
