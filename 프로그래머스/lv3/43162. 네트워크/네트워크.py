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
