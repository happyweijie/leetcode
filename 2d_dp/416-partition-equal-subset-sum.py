class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        """
        2D-DP Solution (Subset Sum Problem)

        Let n = len(nums), S = sum(nums), then
        Time: O(n * S)
        Space: O(n * S)
        """
        total = sum(nums)
        # no way to parition odd total
        if total % 2 == 1:
            return False

        # check if there exists a subset that sums to total / 2
        return self.subset_sum(nums, total // 2)

    def subset_sum(self, nums: list[int], k: int) -> bool:
        n = len(nums)

        # (n + 1) by (k + 1) matrix
        # dp[i][j] means with the first i numbers,
        # is there a subset which sums to j
        dp = [[False] * (k + 1) for _ in range(n + 1)]
        # we can always find a subset which sums to 0
        for i in range(n + 1):
            dp[i][0] = True

        # See if we can reach each j with the first i numbers
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                # Recurrence:
                # dp[i][j]:
                # 1. With i - 1 numbers, we can reach j - nums[i -1]
                # (assume j >= nums[i - 1]). Picking the ith number (nums[i - 1])
                # thus allows us to reach j
                # 2. With i - 1 numbers, we can already reach j. No need
                # to pick nums[i - 1].     
                dp[i][j] = (
                    (dp[i - 1][j - nums[i - 1]] if j >= nums[i - 1] else False) 
                    or 
                    dp[i - 1][j]
                )

        return dp[n][k]
        