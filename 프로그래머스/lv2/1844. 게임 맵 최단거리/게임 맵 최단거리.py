from collections import deque

def solution(maps):
    # maps의 행과 열의 개수 ROW, COL을 저장
    ROW, COL = len(maps), len(maps[0])
    
    # 4가지 방향 (상, 하, 좌, 우)을 나타내는 directions 리스트 생성
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    # 시작점 start와 끝점 end 정의
    start = (0, 0)
    end = (ROW - 1, COL - 1)
    
    # visited 배열 생성. visited[i][j]는 (i, j)에 방문한 적이 있는지 확인
    visited = [[False for _ in range(COL)] for _ in range(ROW)]
    
    # 시작점 start에서의 거리 distance = 1로 시작하여 큐에 추가
    queue = deque([(start, 1)])
    visited[start[0]][start[1]] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 요소(r, c), distance를 꺼냄
        (r, c), distance = queue.popleft()
        # (r, c)가 끝점이면 distance를 반환
        if (r, c) == end:
            return distance
        
        # 4가지 방향에 대하여
        for dr, dc in directions:
            # 새로운 좌표 new_r, new_c를 계산
            new_r, new_c = r + dr, c + dc
            # 새로운 좌표가 범위 내에 있고, 값이 1이고, 방문하지 않았으면
            if 0 <= new_r < ROW and 0 <= new_c < COL and maps[new_r][new_c] == 1 and not visited[new_r][new_c]:
                # 새로운 좌표와 거리 distance + 1
                queue.append(((new_r, new_c), distance + 1))
                visited[new_r][new_c] = True
    
    return -1
