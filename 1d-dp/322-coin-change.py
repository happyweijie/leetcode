class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        """
        Bottom-Up DP solution

        Time: O(amount * c)
        Space: O(amount)
        """
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(amount):
            if dp[i] == -1:
                continue

            for c in coins:
                if i + c <= amount:
                    dp[i + c] = min(dp[i] + 1, dp[i + c])

        return dp[amount] if dp[amount] != float("inf") else -1
