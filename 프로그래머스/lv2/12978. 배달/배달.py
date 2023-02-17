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

"""
Problem: 
- There are N cities numbered from 1 to N, and M bidirectional roads connecting them. 
- Each road has a travel cost. Starting from city 1, you want to visit all cities with the minimum cost possible. 
- Return the minimum cost.

Here's the Python 3 code to solve this problem using Dijkstra's algorithm:
Here's how the code works:
1. First, we create an adjacency list to represent the graph. 
- For each road, we add both directions to the adjacency list.
2. Next, we use Dijkstra's algorithm to find the shortest path from city 1 to all other cities. 
- We initialize the distance to all cities to infinity, except for city 1, which we set to 0. 
- We use a priority queue to keep track of the nodes we need to visit next, with the priority being the distance from city 1.
3. After we have found the shortest distance to each city, we iterate through all cities and count the number of cities that can be visited within K distance.
4. Finally, we return the answer.

Note that this code assumes that the input is valid (e.g., there are no negative costs or cycles in the graph), 
so you may want to add some error checking if necessary.
"""
