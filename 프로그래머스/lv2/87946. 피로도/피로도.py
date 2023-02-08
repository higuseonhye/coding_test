answer = 0
N = 0
visited = []

def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0

def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer

"""
위의 코드는 던전을 탐색하는 깊이 우선 탐색(DFS, Depth-First Search) 알고리즘을 구현한 것입니다.

answer 변수는 탐색한 던전의 최대 개수를 저장합니다.
N 변수는 dungeons 리스트의 길이를 저장합니다.
visited 리스트는 현재 탐색 중인 던전이 방문된 적이 있는지 표시합니다.
dfs 함수는 새로운 던전을 탐색하고, 탐색한 던전의 개수가 현재 가지고 있는 answer 변수보다 크다면 answer를 업데이트 합니다.
solution 함수는 dfs 함수를 사용하여 결과를 반환합니다.
입력으로 k와 dungeons 리스트가 주어지며, 
    solution 함수는 첫 번째 매개변수 k로 주어진 최대 생명력으로 두 번째 매개변수 dungeons로 주어진 던전을 탐색할 수 있는 던전의 최대 개수를 반환합니다.
"""
