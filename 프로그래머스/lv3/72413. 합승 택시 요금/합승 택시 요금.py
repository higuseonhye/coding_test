import heapq

def solution(n, s, a, b, fares):
    # Initialize an adjacency list to represent the graph
    adj_list = [[] for _ in range(n+1)]
    for u, v, w in fares:
        adj_list[u].append((v, w))
        adj_list[v].append((u, w))

    # Define a function to compute the shortest distances from a starting node to all other nodes in the graph
    def dijkstra(start):
        distances = [float('inf')] * (n+1)
        distances[start] = 0
        heap = [(0, start)]
        while heap:
            dist, u = heapq.heappop(heap)
            if dist > distances[u]:
                continue
            for v, w in adj_list[u]:
                if dist + w < distances[v]:
                    distances[v] = dist + w
                    heapq.heappush(heap, (distances[v], v))
        return distances

    # Compute the shortest distances from each node to all other nodes in the graph
    dist = [dijkstra(u) for u in range(n+1)]

    # Initialize the answer with the direct fare from s to a and from s to b
    answer = dist[s][a] + dist[s][b]

    # Try each possible transfer node and update the answer if a better fare is found
    for t in range(1, n+1):
        fare = dist[s][t] + dist[t][a] + dist[t][b]
        answer = min(answer, fare)

    return answer
