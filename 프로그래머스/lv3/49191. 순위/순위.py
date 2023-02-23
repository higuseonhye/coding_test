def solution(n, results):
    win, lose = {}, {}
    
    for i in range(1, n+1):
        win[i], lose[i] = set(), set()

    for i, j in results:
        win[i].add(j)
        lose[j].add(i)

    for i in range(1, n+1):
        for j in win[i]:
            lose[j].update(lose[i])
        for j in lose[i]:
            win[j].update(win[i])

    answer = 0
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1
            
    return answer
