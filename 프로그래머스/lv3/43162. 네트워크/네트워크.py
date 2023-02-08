def solution(n, computers):
    def dfs(node, computers, visited):
        stack = [node]
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                for i, val in enumerate(computers[node]):
                    if val == 1:
                        stack.append(i)

    visited = [False for _ in range(n)]
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i, computers, visited)
    return count

"""
이 코드는 네트워크의 개수를 계산하는 함수입니다.

dfs 함수
- 파라미터: 현재 노드의 번호, 컴퓨터의 정보가 담긴 2차원 배열, 방문 여부가 저장된 리스트
- 깊이 우선 탐색을 이용해 현재 노드와 연결된 노드들을 모두 방문하고, visited 리스트에 표시한다.

solution 함수
- 파라미터: 컴퓨터의 개수, 컴퓨터의 정보가 담긴 2차원 배열
- visited 리스트를 생성하여 모든 노드를 방문하지 않은 것으로 초기화한다.
- count 변수를 생성하여 네트워크의 개수를 저장한다.
- 모든 노드를 반복하여 visited 리스트에 방문하지 않은 것이 있으면, dfs 함수를 실행하고 count 변수를 1 증가시킨다.
- 모든 노드를 반복하여 끝나면 count 변수를 리턴한다.
"""

"""
이 코드는 주어진 네트워크 정보(computers)를 바탕으로 몇 개의 네트워크가 있는지를 계산하는 함수입니다.

1. 함수 dfs(node, computers, visited) : DFS(Depth First Search)를 구현한 함수로, 
    현재 node에서 시작하여 다음 node로 갈 수 있는 모든 node를 방문하고 visited 리스트에 표시합니다.
2. visited 리스트 : 각 node가 방문되었는지 여부를 표시하는 리스트입니다.
3. count 변수 : 네트워크의 개수를 저장하는 변수입니다.
4. for 루프 : 각 node에 대해 방문 여부를 확인하고, 방문하지 않았다면 count를 증가시키고 dfs 함수를 실행합니다.
5. return : count 값을 반환합니다.
'''
