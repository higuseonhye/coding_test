from collections import deque

def solution(maps):
    def bfs(y, x):
        q = deque()
        q.append((y, x, 1))

        while q:
            y, x, distance = q.popleft()

            if y == len(maps)-1 and x == len(maps[0])-1:
                return distance

            if maps[y][x] == 0:
                continue
            maps[y][x] = 0

            if y+1 < len(maps):
                q.append((y+1, x, distance+1))
            if x+1 < len(maps[0]):
                q.append((y, x+1, distance+1))
            if y-1 >= 0:
                q.append((y-1, x, distance+1))
            if x-1 >= 0:
                q.append((y, x-1, distance+1))

        return -1

    return bfs(0, 0)

"""
이 코드는 2차원 맵에서 (0, 0)에서 (len(maps)-1, len(maps[0])-1)까지 가장 짧은 경로의 길이를 구하는 것입니다.

solution 함수는 bfs 함수를 호출하여 결과를 반환합니다. 
- bfs 함수는 2차원 맵에서 (y, x)에서 (len(maps)-1, len(maps[0])-1)까지 가장 짧은 경로의 길이를 계산하는 함수입니다.

bfs 함수는 입력된 y, x 좌표를 큐에 넣고 시작합니다. 
- 그리고 큐에서 원소를 꺼내 (y, x, distance) 좌표와 그 좌표까지의 거리를 가져옵니다. 
- 그러면 maps[y][x] 값이 0이면 (즉, 이미 방문한 좌표) continue하고, 아니면 maps[y][x] = 0으로 맵을 수정하여 다음에 이 좌표를 방문하지 않도록 합니다.

마지막으로, y+1과 y-1, x+1과 x-1이 맵의 범위를 벗어나지 않는 경우 각각 큐에 넣고 distance + 1로 증가시켜 다음 거리를 계산할 수 있도록 합니다
"""
