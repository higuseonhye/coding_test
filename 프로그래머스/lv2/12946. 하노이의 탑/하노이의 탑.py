def solution(n):
    answer = []
    
    def hanoi(n, start, end, via):
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(n-1, start, via, end)
            answer.append([start, end])
            hanoi(n-1, via, end, start)
    
    hanoi(n, 1, 3, 2)
    
    return answer

"""
Here's how the code works:

1. We initialize an empty list answer to store the moves of the Hanoi Tower.

2. We define a recursive function hanoi that takes the following arguments:
    n: the number of disks
    start: the starting peg (1, 2, or 3)
    end: the ending peg (1, 2, or 3)
    via: the intermediate peg (1, 2, or 3)

3. If n is 1, we simply append the move to answer (moving from start to end).

4. If n is greater than 1, we first move n-1 disks from start to via using end as the intermediate peg (recursive call).

5. We then move the remaining disk from start to end and append the move to answer.

6. Finally, we move the n-1 disks from via to end using start as the intermediate peg (recursive call).

7. We call hanoi with the initial parameters (n=number of disks, start=1, end=3, via=2) to solve the Hanoi Tower problem and fill answer with the moves.

8. We return answer as the list of moves to solve the problem.
"""
