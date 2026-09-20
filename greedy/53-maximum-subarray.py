from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Kadane's algorithm (Greedy)

        Time complexity: O(n), where n is the length of the input list.
        Space complexity: O(1).
        """
        # track the current sum and the maximum sum found so far
        cur_sum = 0
        res = float("-inf")

        for n in nums:
            cur_sum += n
            res = max(res, cur_sum)

            # reset the current sum to 0 if it becomes negative
            # negative current sum will not contribute to the maximum sum.
            if cur_sum < 0:
                cur_sum = 0

        return res

class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Divide and conquer approach
        Time complexity: O(n log n), where n is the length of the input list.
        Space complexity: O(log n), due to the recursive call stack.
        """
        return self.maxSubArrayRec(nums, 0, len(nums) - 1)

    def maxSubArrayRec(self, nums: List[int], lo: int, hi: int) -> int | float:
        if hi < lo:
            return float("-inf")
        elif lo == hi:
            return nums[lo]

        mid = (lo + hi) // 2
        left_sum = self.maxSubArrayRec(nums, lo, mid)
        right_sum = self.maxSubArrayRec(nums, mid + 1, hi)

        cross_sum = self.maxCrossSum(nums, lo, hi)

        return max(left_sum, right_sum, cross_sum)

    def maxCrossSum(self, nums: List[int], lo: int, hi: int) -> int:
        mid = (lo + hi) // 2

        left_max = float("-inf")
        cur_sum = 0
        for i in range(mid, lo - 1, -1):
            cur_sum += nums[i]
            left_max = max(left_max, cur_sum)

        right_max = float("-inf")
        cur_sum = 0
        for j in range(mid + 1, hi + 1):
            cur_sum += nums[j]
            right_max = max(right_max, cur_sum)

        return left_max + right_max

class Solution3:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Brute force approach (TLE)
        Time complexity: O(n^2), where n is the length of the input list.
        Space complexity: O(1).
        """
        res = float("-inf")
        for i in range(len(nums)):
            cur = 0

            for j in range(i, len(nums)):
                cur += nums[j]
                res = max(cur, res)

        return res
    