import heapq

def solution(N, road, K):
    # create an adjacency list to represent the graph
    graph = {i: [] for i in range(1, N+1)}
    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))

    # use Dijkstra's algorithm to find the shortest path from city 1 to all other cities
    distances = {i: float('inf') for i in range(1, N+1)}
    distances[1] = 0
    pq = [(0, 1)]
    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, cost in graph[node]:
            new_cost = distances[node] + cost
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor))

    # count the number of cities that can be visited within K distance
    answer = 0
    for i in range(1, N+1):
        if distances[i] <= K:
            answer += 1

    return answer
