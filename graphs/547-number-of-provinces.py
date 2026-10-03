from collections import deque

class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        """
        Problem is finding the number of connected components 
        in an undirected graph (represented as an adjacency matrix). 
        
        Algorithm: Run DFS/BFS from each unvisited vertex, marking all reachable vertices as visited.

        Time: O(n^2)
        Space: O(n) for the visited array
        """
        self.provinces = 0
        n = len(isConnected)
        visited = [False] * n

        def dfs(u: int) -> None:
            visited[u] = True

            for v in range(n):
                if not visited[v] and isConnected[u][v]:
                    dfs(v)

        for u in range(n):
            if not visited[u]:
                dfs(u)
                self.provinces += 1

        return self.provinces

    from collections import deque

class Solution2:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        """
        BFS Approach
        """
        self.provinces = 0
        n = len(isConnected)
        visited = [False] * n

        def bfs(s: int) -> None:
            q = deque([s])
            visited[s] = True

            while q:
                u = q.popleft()

                for v in range(n):
                    if not visited[v] and isConnected[u][v]:
                        visited[v] = True
                        q.append(v)

        for u in range(n):
            if not visited[u]:
                bfs(u)
                self.provinces += 1

        return self.provinces
