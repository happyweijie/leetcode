import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Convert edge list to adjacency list
        adj_list = [[] for _ in range(n)]
        for u, v, w in times:
            adj_list[u - 1].append((w, v - 1))

        # Dijkstra's Algorithm
        dist = [float('inf')] * n
        dist[k - 1] = 0

        pq = [(dist[k - 1], k - 1)]

        while pq:
            cost, cur = heapq.heappop(pq)

            if cost != dist[cur]:
                continue

            for weight, nei in adj_list[cur]:
                if dist[cur] + weight < dist[nei]:
                    dist[nei] = dist[cur] + weight
                    heapq.heappush(pq, (dist[nei], nei))

        # Return -1 if any vertice is unreachable
        # otherwise minimum time for all nodes to receive signal
        # is the longest of all the shortest paths
        return -1 if any(d == float('inf') for d in dist) else max(dist)

