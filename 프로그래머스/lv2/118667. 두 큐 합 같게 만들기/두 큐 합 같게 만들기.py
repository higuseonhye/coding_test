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


"""
from collections import deque                                       # import deque from collections module
from typing import List                                             # import List from typing module

def find_min_moves(queue1: List[int], queue2: List[int]) -> int:
    q = deque(queue1 + queue2)                                      # concatenate queue1 and queue2 and create a deque object
    target = sum(q) // 2                                            # calculate the target sum

    left, right = 0, len(queue1) - 1                                # set left pointer to 0 and right pointer to len(queue1) - 1
    curr_sum = sum(queue1)                                          # initialize current sum to the sum of queue1
    count = 0                                                       # initialize counter to 0

    while left < len(q) and right < len(q):                         # continue loop until both pointers are less than length of q
        if curr_sum == target:                                      # if the current sum equals the target sum
            return count                                            # return the number of moves taken

        elif curr_sum < target and right < len(q) - 1:              # if the current sum is less than target sum and the right pointer is less than len(q) - 1
            right += 1                                              # move right pointer to the right
            curr_sum += q[right]                                    # add the new element to the current sum

        else:                                                       # otherwise
            curr_sum -= q[left]                                     # subtract the left element from the current sum
            left += 1                                               # move the left pointer to the right

        count += 1                                                  # increment the counter

    return -1                                                       # return -1 if no solution found
"""
