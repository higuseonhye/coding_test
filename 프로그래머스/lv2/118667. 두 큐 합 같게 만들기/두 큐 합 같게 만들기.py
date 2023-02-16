from collections import deque
from typing import List

def solution(queue1: List[int], queue2: List[int]) -> int:
    q = deque(queue1 + queue2)
    target = sum(q) // 2

    left, right = 0, len(queue1) - 1
    curr_sum = sum(queue1)
    count = 0

    while left < len(q) and right < len(q):        
        if curr_sum == target:
            return count

        elif curr_sum < target and right < len(q) - 1:
            right += 1
            curr_sum += q[right]

        else:
            curr_sum -= q[left]
            left += 1

        count += 1

    return -1
