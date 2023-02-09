def solution(land):
    for i in range(len(land) - 2, -1, -1):
        for j in range(4):
            land[i][j] += max(land[i + 1][:j] + land[i + 1][j + 1:])
    return max(land[0])
