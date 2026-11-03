class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        2D-Dynamic Programming Bottom-Up
        Time: O(n * m)
        Space: O(n * m)

        Optimisation: Keep only 2 rows then we can reduce
        our space to O(min(n, m))
        """
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # find the lcs of the first i characters of text1
        # and first j characters of text2
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # if ith char of text1 == jth char of text 2
                # (text1[i - 1] == text2[j - 1])
                # our subproblem is finding the LCS of
                # the first (i-1) chars of text1 and first
                # (j-1) chars of text2
                s1 = 1 + (
                    dp[i - 1][j - 1] 
                    if text1[i - 1] == text2[j - 1] 
                    else float("-inf") # s1 is invalid if chars not equal
                )

                # otherwise, because the chars are not equal
                # then we either don't pick
                # ith char of text1 or jth char of text2 
                # in our LCS
                s2 = max(dp[i][j - 1], dp[i - 1][j])
                dp[i][j] = max(s1, s2)

        return dp[n][m]
