from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        visited = set() # vertices visited are our suspicious methods
        indegree = [0] * n
        adj_list = [[] for _ in range(n)]
        
        for a, b in invocations:
            adj_list[a].append(b)
            indegree[b] += 1
            
        def dfs(u: int) -> None:
            visited.add(u) # u is reachable so it is suspicious
            
            for v in adj_list[u]:
                indegree[v] -= 1 # decrement indegree
                
                if v not in visited:
                    dfs(v)
        
        # use dfs/bfs from k to find methods invoked by it
        # those are suspicious
        dfs(k)

        # if any suspicious methods does not have indegree 0
        # then it is invoked by some other regular method
        # cannot remove the group, so return all methods
        if any(indegree[i] != 0 for i in visited):
            return list(range(n))
        
        # otherwise return all non sus methods
        return [
            i for i in range(n)
            if i not in visited
        ]
