from functools import cache
from typing import List

class Solution:
    """
    Bottom up tabulation,
    just store prev 2 houses instead of whole dp table
    This works because we only need the 2 previous states

    O(N) approach
    O(1) space
    """
    def rob(self, nums: List[int]) -> int:
        # just store prev 2 houses
        # instead of whole dp table

        # no house
        prev2 = 0
        # 1 house -> can only rob first house
        prev1 = nums[0]

        for i in range(2, len(nums) + 1):
            # we can either rob the last house (skip this house)
            # or rob this house 
            prev1, prev2 = max(prev1, prev2 + nums[i - 1]), prev1

        return prev1

    """
    Bottom up tabulation with table

    O(N) approach
    O(N) space
    """
    def rob(self, nums: List[int]) -> int:
        # the number of money we can rob
        # from the first i houses
        dp = [0] * (len(nums) + 1)

        # no house
        dp[0] = 0
        # 1 house -> can only rob first house
        dp[1] = nums[0]

        for i in range(2, len(nums) + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i - 1])

        return dp[-1]

    # recursive
    def rob2(self, nums: List[int]) -> int:
        return self.rob_rec_memo(tuple(nums), len(nums) -1)

    """
    recursive top-down
    """
    def rob_rec(self, nums, idx):
        if idx < 0:
            return 0

        return max(
            self.rob_rec(nums, idx - 2) + nums[idx],
            self.rob_rec(nums, idx - 1)
        )

    """
    recursive top-down + memo
    """
    @cache
    def rob_rec_memo(self, nums, idx):
        if idx < 0:
            return 0

        return max(
            self.rob_rec(nums, idx - 2) + nums[idx],
            self.rob_rec(nums, idx - 1)
        )
    