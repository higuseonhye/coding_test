def solution(n, computers):
    def dfs(node, computers, visited):
        visited[node] = True
        for i, val in enumerate(computers[node]):
            if val == 1 and not visited[i]:
                dfs(i, computers, visited)
                
    visited = [False for _ in range(n)]
    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            dfs(i, computers, visited)
    return count
