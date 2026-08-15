from collections import deque
from typing import List

class Solution:
    DIRS = [
        (1, 0),
        (-1, 0),
        (0, -1),
        (0, 1)
    ]

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.

        Time: O(M * N)
        Space: O(M * N)
        """
        # cell dimensions
        m = len(board)
        n = len(board[-1])

        # A region is a connected component of Os

        visited = set()
        def bfs(i: int, j: int) -> list[tuple[int, int]]:
            # run bfs starting from (i, j) adding all O cells
            q = deque([(i, j)])
            visited.add((i, j))
            
            region = [] # track cells in current connected component
            region.append((i, j))

            while q:
                r, c = q.popleft()
                
                for dr, dc in self.DIRS:
                    nr, nc = r + dr, c + dc

                    # skip invalid
                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    # skip x and alr visited
                    if board[nr][nc] == "X" or (nr, nc) in visited:
                        continue

                    q.append((nr, nc))
                    region.append((nr, nc))
                    visited.add((nr, nc))

            return region

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i, j) not in visited:
                    # All O cells reachable from (i, j)
                    region =  bfs(i, j)

                    # cannot surround if an O cell is at the edge
                    if any(self.is_edge_cell(r, c, m, n) for r, c in region):
                        continue

                    # surround that region by making everything X
                    for r, c in region:
                        board[r][c] = "X"

        # done
        """
        Alt solution:
        Track every cell in the edge of the board looking for Os
        -> For each O on the edge, run BFS/DFS from it and add
        all O cells traversed to a visited set
        -> Those O cells are "safe", cannot be replaced

        Iterate over the non-edge cells:
            for each O cell encountered:
                if cell is not in visited:
                    board[cell] = "X"

        Time: O(M * N)
        Space: O(M * N)
        -> This solution is slightly better in best cases
        as the visited set does not need to store every single O
        just those that cannot be surrounded/flipped to X
        """

    def is_edge_cell(self, r: int, c: int, m: int, n: int) -> bool:
        return r == 0 or r == m - 1 or c == 0 or c == n - 1
        