class Solution:
    KEYS = [
        "",
        "",
        "abc",
        "def",
        "ghi",
        "jkl",
        "mno",
        "pqrs",
        "tuv",
        "wxyz"
    ]

    def letterCombinations(self, digits: str) -> list[str]:
        """
        Backtracking solution

        Let n be length of digits.
        Time: O(4^n), worst case 4 choices for each digit (7/9)
        Space: O(n) for recursion stack
        """
        res = []

        def backtrack(idx: int, combi: list[str]) -> None:
            # add to res once we run out of digits
            if idx == len(digits):
                res.append("".join(combi))
                return

            key = int(digits[idx])
            for letter in self.KEYS[key]:
                combi.append(letter)
                backtrack(idx + 1, combi)
                combi.pop()
        
        backtrack(0, [])
        return res
        