from collections import deque

def solution(maps):
    ROW, COL = len(maps), len(maps[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    start = (0, 0)
    end = (ROW - 1, COL - 1)
    visited = [[False for _ in range(COL)] for _ in range(ROW)]
    queue = deque([(start, 1)])
    visited[start[0]][start[1]] = True
    
    while queue:
        (r, c), distance = queue.popleft()
        if (r, c) == end:
            return distance
        
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if 0 <= new_r < ROW and 0 <= new_c < COL and maps[new_r][new_c] == 1 and not visited[new_r][new_c]:
                queue.append(((new_r, new_c), distance + 1))
                visited[new_r][new_c] = True
    
    return -1
