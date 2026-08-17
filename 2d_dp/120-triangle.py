from typing import List
from functools import cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        Bottom-Up DP In-place (Mutates the triange)

        Time: O(n^2)
        Space: O(1)
        """
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                # cell j is is reachable from j and j + 1 in the next row
                triangle[i][j] = min(
                    triangle[i][j] + triangle[i + 1][j],
                    triangle[i][j] + triangle[i+ 1][j + 1]
                ) 

        return triangle[0][0]
    
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        """
        Bottom-Up DP In-place with tabulation

        Time: O(n^2)
        Space: O(n)
        """
        n = len(triangle)
        # track the minimum to cost to column i in the current row
        # initially very value is the last row
        dp = list(triangle[-1])

        # bottom-up dp
        for i in range(n - 2, -1, -1):
            for j in range(len(triangle[i])):
                # j is is reachable from j and j + 1 in the next row
                # relax using the value stored in dp[j] and dp[j + 1]
                dp[j] = min(
                    triangle[i][j] + dp[j],
                    triangle[i][j] + dp[j + 1]
                )

        return dp[0]

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        """
        Top-down DP with memoization

        Time: O(n^2)
        Space: O(n^2)
        """
        
        @cache
        def dfs(i: int, j: int):
            # return once we reach the bottom of the triangle
            if i == len(triangle):
                return 0
                
            return min(
                triangle[i][j] + dfs(i + 1, j),
                triangle[i][j + 1] + dfs(i + 1, j + 1)
            )
        
        # We start from triangle[0][0]
        # the very top of the triangle
        return triangle[0][0] + dfs(1, 0)

    def minimumTotal3(self, triangle: List[List[int]]) -> int:
            """
            Top-down Recursion
    
            Time: O(2^n)
            Space: O(n), space for recursion stack
            """
            
            def dfs(i: int, j: int):
                # return once we reach the bottom of the triangle
                if i == len(triangle):
                    return 0
                    
                return min(
                    triangle[i][j] + dfs(i + 1, j),
                    triangle[i][j + 1] + dfs(i + 1, j + 1)
                )
            
            # We start from triangle[0][0]
            # the very top of the triangle
            return triangle[0][0] + dfs(1, 0)
