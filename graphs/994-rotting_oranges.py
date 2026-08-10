from collections import deque
from typing import List

class Solution:
    
    DIRS = [
        (1, 0),
        (-1, 0),
        (0, -1),
        (0, 1)
    ]
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        q = deque() # all rotten oranges initially
        count = 0 # track no of fresh oranges
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    count += 1
                
        mins = 0

        # BFS Algorithm
        # Stop looping when there are no more rotten oranges to process 
        # or all fresh oranges have rotted (edge case: no fresh oranges to begin with)
        while q and count != 0:

            for _ in range(len(q)):
                r, c  = q.popleft()
                
                for dr, dc in self.DIRS:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nr >= m or nc < 0 or nc >= n: 
                        continue
                        
                    if grid[nr][nc] == 1:
                        count -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            
            mins += 1
                
        return mins if count == 0 else -1
        