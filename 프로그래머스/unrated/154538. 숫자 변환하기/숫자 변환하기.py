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

"""
Problem: Given three integers x, y, and n, you want to transform x to y using the following operations:

Add n to x
Multiply x by 2
Multiply x by 3
Write a function in Python to return the minimum number of operations needed to transform x to y. If it is impossible to transform x to y, return -1.

Here's a Python 3 code to solve this problem using Breadth-First Search (BFS):
Here's how the code works:

1. If x is already equal to y, we return 0, as no operations are needed.

2. We use a queue to perform a BFS traversal of the state space. 
- Each element in the queue is a tuple (curr, count), where curr is the current number and count is the number of operations performed so far.

3. We also use a set visited to keep track of the numbers that have already been visited, to avoid cycles and unnecessary computations.

4. At each step, we generate the next possible numbers by performing the three operations, 
   and add them to the queue if they have not been visited yet and are not greater than y.

5. If we encounter y during the BFS traversal, we return the number of operations performed so far.

6. If we exhaust the queue without finding y, we return -1, indicating that it is impossible to transform x to y.

Note that this code assumes that the input is valid, so you may want to add some error checking if necessary.
"""
