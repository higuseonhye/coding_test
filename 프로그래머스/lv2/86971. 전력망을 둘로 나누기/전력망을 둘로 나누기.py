def solution(n, wires):
    answer = n
    
    # Try removing each wire one at a time and count the number of nodes in the largest connected component
    for i in range(n-1):
        # Remove the i-th wire and create an adjacency list representing the remaining graph
        adj_list = [[] for _ in range(n+1)]
        for j, (u, v) in enumerate(wires):
            if j == i:
                continue
            adj_list[u].append(v)
            adj_list[v].append(u)

        # Perform a depth-first search on each node to compute the size of the connected component
        component_sizes = []
        visited = [False] * (n+1)
        for u in range(1, n+1):
            if not visited[u]:
                stack = [u]
                visited[u] = True
                component_size = 1
                while stack:
                    u = stack.pop()
                    for v in adj_list[u]:
                        if not visited[v]:
                            stack.append(v)
                            visited[v] = True
                            component_size += 1
                component_sizes.append(component_size)

        # Compute the difference between the sizes of the two connected components
        diff = abs(component_sizes[0] - component_sizes[1])
        answer = min(answer, diff)

    return answer
