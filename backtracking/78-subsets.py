from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Time Complexity: O(2^n * n)
        There are 2^n subsets, each element is a choice to take/dont take,
        copying takes O(n) time worst case
        Space: O(2^n * n)
        """
        # start with empty subset
        cur = [] 
        res = [[]]

        def backtrack(start: int) -> None:
            for i in range(start, len(nums)):
                cur.append(nums[i])

                # new subset
                res.append(cur.copy())

                backtrack(i + 1)

                cur.pop()
        
        backtrack(0)
        return res