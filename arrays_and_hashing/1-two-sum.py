from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(n)
        Space: O(n), store the index of each number in a hash table
        """
        # store the index of each number in a hash table
        num_to_index = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_to_index:
                return [num_to_index[diff], i]

            if nums[i] not in num_to_index:
                num_to_index[nums[i]] = i

    def twoSumBruteForce(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(n^2)
        Space: O(1)
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSumTwoPointers(self, nums: List[int], target: int) -> List[int]:
        """
        Time: O(n log n), due to sorting the array first
        Space: O(n), need to store the original indices of the numbers
        """
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort(key=lambda x: x[0])

        left, right = 0, len(nums_with_index) - 1

        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]

            if current_sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
            