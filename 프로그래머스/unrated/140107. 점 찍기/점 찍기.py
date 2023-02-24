def solution(k, d):
    answer, d_square = 0, d ** 2
    for i in range(0, d + 1, k):
        answer += int((d_square - i ** 2) ** .5) // k + 1
    return answer

