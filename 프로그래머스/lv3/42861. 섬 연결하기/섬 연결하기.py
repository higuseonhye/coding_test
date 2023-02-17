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
