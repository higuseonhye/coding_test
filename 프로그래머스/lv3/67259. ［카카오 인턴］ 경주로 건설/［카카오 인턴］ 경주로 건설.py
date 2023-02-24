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

"""
1. Import the deque class from the collections module.
- Define the solution function that takes a board parameter.
- Get the size of the board and set the infinity constant.
- Create a 3D array of cost with dimensions (n, n, 4) to store the minimum cost to reach each point with each direction.
- Define the dx and dy arrays to represent the change in x and y coordinates for each of the four directions (right, down, left, up).

2. Initialize the minimum cost for each direction at the starting point (0, 0).
- Create an empty deque object q and add the starting point with an invalid direction -1 to it.

3. While q is not empty, pop the leftmost element and assign its x-coordinate, y-coordinate, and direction to x, y, and d.
- For each of the four directions, calculate the new coordinates nx and ny.
- If the new coordinates are outside the board or are blocked by a wall, skip to the next direction.
- Calculate the new cost to reach the new point based on the previous direction.
- If the new cost is smaller than the previous cost, update the minimum cost in the cost array and add the new point to q.
- Repeat this process until q is empty.

4. Return the minimum cost to reach the bottom-right corner (n-1, n-1) of the board.
"""
