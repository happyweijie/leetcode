class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Levenshtein's Distance Dynamic Programming

        Time: O(mn)
        Space: O(m), just store 2 rows instead of whole matrix
        """
        n, m = len(word1), len(word2)

        # first row is cost to transform empty word1 to 
        # first j characters of word2
        # this requires j insertions
        dp = [list(range(m + 1))]

        for i in range(1, n + 1):
            dp.append([0] * (m + 1))
            # base case: first col is cost to transform 
            # first i characters of word1 to empty word2
            # this requires i deletion
            dp[1][0] = i

            for j in range(1, m + 1):
                # cost of substitution (0 if chars are equal)
                substitution = 0 if word1[i - 1] == word2[j - 1] else 1
                
                dp[1][j] = min(
                    dp[0][j - 1] + substitution, # substitution
                    1 + dp[1][j - 1], # addition
                    1 + dp[0][j] # deletion
                )
            
            # pop off 1st row, no longer needed
            dp.pop(0)

        return dp[-1][-1]

class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        Levenshtein's Distance Dynamic Programming

        Time: O(mn)
        Space: O(mn), store whole matrix
        """
        n, m = len(word1), len(word2)

        # initialize matrix
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # base case
        # first row is cost to transform empty word1 to 
        # first j characters of word2
        # this requires j insertions
        dp[0] = list(range(m + 1))
        # first col is cost to transform 
        # first i characters of word1 to empty word2
        # this requires i deletions
        for i in range(n + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # cost of substitution (0 if chars are equal)
                substitution = 0 if word1[i - 1] == word2[j - 1] else 1
                
                dp[i][j] = min(
                    dp[i - 1][j - 1] + substitution, # substitution
                    1 + dp[i][j - 1], # addition
                    1 + dp[i - 1][j] # deletion
                )

        return dp[-1][-1]
    