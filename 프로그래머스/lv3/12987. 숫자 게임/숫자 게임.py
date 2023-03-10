def solution(A, B):
    A.sort()
    B.sort()
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            i += 1
        j += 1
    return i

"""
1. solution 함수는 2개의 인자 A, B 를 받습니다. 이 두 리스트는 각각 남자와 여자의 성적을 나타냅니다.
2. A, B 두 리스트를 오름차순으로 정렬합니다.
3. i, j 변수는 각각 남자와 여자의 리스트를 탐색할 때 사용할 인덱스를 나타냅니다.
4. while 루프는 i 가 A 리스트의 길이보다 작고 j 가 B 리스트의 길이보다 작을 때 반복합니다.
5. if 문에서 A[i] < B[j] 조건이 참이면 i 를 1 증가시킵니다. 그렇지 않으면 j 만 1 증가시킵니다.
6. 루프가 끝나면 i 값을 반환합니다. 이 값은 남자와 여자 중 남자의 최대 수가 선발될 수 있는 수를 나타냅니다.
"""
