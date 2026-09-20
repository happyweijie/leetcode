from collections import defaultdict, deque
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        Graph:
        Vertices: Variables, e.g. a, b, c etc.
        Edges: Directed edges based of equations and values
        1. a_i -> b_i: values[i]
        2. b_i -> a_i: 1 / values[i]

        Solution:
        For each query:
            run bfs from c to d
            update cost along the way -> cache[c][nei] = cache[c][node] * cost

        Time: 
        Let V be number of variables and E be number of equations
        Time: O(q * (V + E))
        Space: O(V^2) for cache
        """
        # Build Graph as an adjancency list
        # Edges are the values of a / b
        adj_list: dict[str, list[tuple[float, str]]] = defaultdict(list)
        for eqn, val in zip(equations, values):
            a, b = eqn

            adj_list[a].append((val, b))
            adj_list[b].append((1 / val, a))

        res = []
        # Cache result values
        cache: dict[str, dict[str, float]] = defaultdict(dict)
        for c, d in queries:
            if c not in adj_list or d not in adj_list:
                res.append(-1.0)
                continue

            if c in cache and d in cache[c]:
                res.append(cache[c][d])
                continue
            elif d in cache and c in cache[d]:
                res.append(1 / cache[d][c])
                continue

            # Run bfs from c
            q = deque([c])
            visited = set([c])
            cache[c][c] = 1

            while q:
                cur = q.popleft()

                for cost, nei in adj_list[cur]:
                    if nei in visited:
                        continue

                    # Calculate c / nei
                    # for a/b and b/c, a/b * b/c = a/c
                    cache[c][nei] = cache[c][cur] * cost

                    # Add nei to queue
                    q.append(nei)
                    visited.add(nei)

            if d not in visited:
                cache[c][d] = -1

            res.append(cache[c][d])
            
        return res
