from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [-1] * (n+1)
    visited[1] = 0
    
    queue = deque([1])
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[node] + 1
                queue.append(neighbor)
    
    max_distance = max(visited)
    answer = 0
    for distance in visited:
        if distance == max_distance:
            answer += 1
    
    return answer
