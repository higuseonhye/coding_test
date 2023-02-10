def solution(A, B):
    A.sort()
    B.sort()
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        j += 1
    return i
