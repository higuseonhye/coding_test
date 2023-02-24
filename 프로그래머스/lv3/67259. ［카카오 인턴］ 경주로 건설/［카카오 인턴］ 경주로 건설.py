from collections import deque

def solution(board):
    n = len(board)
    INF = float('inf')
    # cost[i][j][k] represents the minimum cost to reach (i, j) with direction k
    cost = [[[INF]*4 for _ in range(n)] for _ in range(n)]
    # directions: right=0, down=1, left=2, up=3
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    # initialize starting points
    for k in range(4):
        cost[0][0][k] = 0
    
    q = deque()
    q.append((0, 0, -1))  # (x, y, direction)
    
    while q:
        x, y, d = q.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or board[nx][ny] == 1:
                continue
            
            # calculate new cost
            if d == -1 or d == i:
                new_cost = cost[x][y][d] + 100
            else:
                new_cost = cost[x][y][d] + 600
            
            if new_cost < cost[nx][ny][i]:
                cost[nx][ny][i] = new_cost
                q.append((nx, ny, i))
    
    return min(cost[n-1][n-1])
