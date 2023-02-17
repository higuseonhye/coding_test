def solution(n, costs):
    # sort the edges by their weight in ascending order
    costs.sort(key=lambda x: x[2])

    # initialize the parent array and rank array for union-find
    parent = [i for i in range(n)]
    rank = [0] * n

    # define the find and union functions for union-find
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x == root_y:
            return False
        if rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            if rank[root_x] == rank[root_y]:
                rank[root_y] += 1
        return True

    # use Kruskal's algorithm to find the minimum spanning tree
    total_cost = 0
    for a, b, cost in costs:
        if union(a, b):
            total_cost += cost

    return total_cost

"""
Problem: There are N islands numbered from 1 to N, and M bridges connecting them. 
Each bridge has a construction cost. 
You want to connect all islands with the minimum cost possible. Return the minimum cost.

Here's the Python 3 code to solve this problem using Kruskal's algorithm:

Here's how the code works:
1. First, we sort the edges by their weight in ascending order.

2. Next, we initialize the parent array and rank array for union-find. 
- The parent array stores the parent node of each node in the tree. Initially, each node is its own parent. 
- The rank array stores the rank of each node, which is used to optimize the union operation.

3. We define the find and union functions for union-find. 
- The find function finds the parent of a node and applies path compression to optimize future find operations. 
- The union function unions two nodes by finding their roots and merging the trees together. 
- It also applies rank optimization to keep the tree balanced.

4. We use Kruskal's algorithm to find the minimum spanning tree. 
- We iterate through the edges in ascending order and add each edge to the tree if it does not create a cycle. 
- To check for cycles, we use the union function to merge the trees that contain the two endpoints of the edge. 
- If the union is successful, we add the weight of the edge to the total cost of the tree.

5. Finally, we return the total cost of the minimum spanning tree.

Note that this code assumes that the input is valid (e.g., there are no negative costs or disconnected islands), 
so you may want to add some error checking if necessary.
"""
