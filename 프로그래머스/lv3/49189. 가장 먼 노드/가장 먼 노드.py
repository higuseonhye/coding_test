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

"""
The solution function takes in an integer n and a list of edges edge. 
The goal of the function is to find the number of nodes that are farthest away from node 1, which is at the root of the tree. 
The function returns this count as an integer.

The function begins by creating a graph using a defaultdict, which allows us to easily create an adjacency list. 
The graph dictionary is constructed by iterating through the list of edges edge, and appending the neighbors of each node to the adjacency list for that node. 
Note that since the graph is undirected, we add each node as a neighbor for the other node as well.

The visited list keeps track of the minimum distance from the root node to each node in the graph. 
It is initialized to -1 for each node except the root node, which is given a distance of 0. 
The queue is initialized with just the root node.

The while loop will run until the queue is empty. 
At each iteration, we pop a node off the left of the queue and iterate through its neighbors. 
For each neighbor, we check if it has been visited yet by seeing if its distance is -1. 
If it hasn't been visited, we update its distance as the distance to the current node + 1 (since the edge connecting them has length 1), and add it to the queue.

Once the BFS has been completed, the visited list now contains the minimum distance from the root node to each node. 
We find the maximum distance, and then iterate through the visited list to find the number of nodes that are farthest away from the root. 
If the distance of a node matches the maximum distance, we increment the answer counter.

Finally, we return the answer counter as the solution to the problem.
"""
