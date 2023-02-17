from collections import deque

def solution(x, y, n):
    if x == y:
        return 0
    queue = deque([(x, 0)])
    visited = set([x])
    while queue:
        curr, count = queue.popleft()
        if curr == y:
            return count
        add = curr + n
        mul2 = curr * 2
        mul3 = curr * 3
        for nxt in [add, mul2, mul3]:
            if nxt <= y and nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, count+1))
    return -1
