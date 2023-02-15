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
