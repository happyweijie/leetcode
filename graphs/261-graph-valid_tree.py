"""
You are given a graph with n nodes labeled from 0 to n - 1. 

You also receive a list of edges where each edge edges[i] = [ai, bi] 
represents an undirected connection between nodes ai and bi.

Your task is to determine if these edges form a valid tree. 

Return true if the graph is a valid tree, and false otherwise.

A valid tree must satisfy these properties:
1. It must be connected (all nodes are reachable from any other node)
2. It must have no cycles (there's exactly one path between any two nodes)
3. For n nodes, a tree must have exactly n - 1 edges
"""
def graph_valid_tree(n: int, edges: list[list[int]]) -> bool:
    """
    Let n = number of vertices, e = number of edges

    Time Complexity: O(n), 
    Explanation: the for loop runs for every edge and only when the graph has 
    exactly n - 1 edges. 
    Removing the if condition, the for loop runs for every edge, so O(e).

    Space Complexity: O(n), space for union-find data structure
    """
    # if the graph does not have exactly n - 1 edges,
    # it is either not connected or has a cycle
    if len(edges) != n - 1:
        return False

    ufds = UnionFind(n)

    for u, v in edges:
        # if u and v are already in the same set, 
        # then adding this edge would create a cycle (not a tree)
        if ufds.is_same_set(u, v):
            return False

        ufds.union(u, v)
        
    return True

class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, u: int) -> int:
        if self.parent[u] == u:
            return u

        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def is_same_set(self, u: int, v: int) -> bool:
        return self.find(u) == self.find(v)
        
    def union(self, u: int, v: int) -> None:
        if self.is_same_set(u, v):
            return
            
        x, y = self.find(u), self.find(v)
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[x] = y

            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

if __name__ == "__main__":
    n = int(input())
    edges = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = graph_valid_tree(n, edges)
    print("true" if res else "false")
