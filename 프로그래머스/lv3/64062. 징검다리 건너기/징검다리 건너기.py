def check(stones, k, mid):
    cnt = 0
    for s in stones:
        if s < mid:
            cnt += 1
        else:
            cnt = 0
        if cnt >= k:
            return False
    return True

def solution(stones, k):
    left, right = 1, max(stones)
    while left <= right:
        mid = (left + right) // 2
        if check(stones, k, mid):
            left = mid + 1
        else:
            right = mid - 1
    return left - 1


"""
이진 검색 알고리즘
- 배열이나 리스트와 같은 정렬된 데이터에서 원하는 값을 찾는 알고리즘 
- 검색 범위를 반으로 나누어 탐색해나가는 방식으로 동작
- 시간 복잡도가 O(log n)으로 매우 빠르게 값을 찾을 수 있음

검색 범위의 시작점은 1로, 돌다리 위의 가장 많은 돌의 수로 끝점을 설정
- 검색 범위를 반으로 나누어가면서 이진 검색 알고리즘을 수행

각 반복에서는 'check' 함수를 사용하여 돌다리를 건너려는 사람의 수가 가능한지를 확인
- 'check' 함수는 현재 검색 범위에서 시도할 수 있는 인원수(mid)를 매개변수로 받아, 
- mid 명의 인원이 k 번 이상 연속해서 돌다리를 건널 수 있는지 확인
- mid 명의 인원이 k 번 이상 연속해서 돌다리를 건널 수 없다면, mid-1 명의 인원까지는 가능하다는 것을 알 수 있음
- 반대로 mid 명의 인원이 k 번 이상 연속해서 돌다리를 건널 수 있다면, mid+1 명의 인원부터 가능하다는 것을 알 수 있음
"""
