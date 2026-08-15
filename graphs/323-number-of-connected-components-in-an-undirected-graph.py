from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Union-Find based solution,
        Define a standard Union Find using union by rank/size
        -> track count in the UnionFind, which represents the number of connected components
        -> initialise count to N (number of vertices)
        -> whenever we union 2 vertices u, v which are not already connected to each (in the same set), count decreases by 1 (number of connected components goes down by 1)


        Time: O(N + E), time to initialise Union Find + time to union all edges
        Space: O(N), space for Union Find
        """
        ufds = UnionFind(n) # O(N)

        for u, v in edges: # O(E)
            ufds.union(u, v)
        
        return ufds.get_count()

class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        self.count = n

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

        # when we union two (disjoint) vertices,
        # the number of connected components goes down.
        self.count -= 1

    def get_count(self) -> int:
        return self.count 
    