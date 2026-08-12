from collections import Counter
from typing import List

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        Sliding window + Hashmap Solution:
        Time: O(n)
        Space: O(n)
        """
        # sliding window
        left = 0
        counter = Counter([nums[left]])
        res = 1 # since k >= 1, smallest possible value for res is 1
        
        for right in range(1, len(nums)):
            
            while counter[nums[right]] + 1 > k:
                # shift left sliding window 
                counter[nums[left]] -= 1 # decrement counter first
                left += 1

            counter[nums[right]] += 1
            
            subarr_len = right - left + 1
            res = max(res, subarr_len)
                
        return res

    def maxSubarrayLengthBruteForce(self, nums: List[int], k: int) -> int:
        """
        Brute force solution
        Time: O(n^2)
        Space: O(n)
        """
        res = 0
        
        for i in range(len(nums)):
            counter = Counter([nums[i]])
            
            j = i + 1
            while j < len(nums):
                if counter[nums[j]] + 1 > k:
                    break
                    
                counter[nums[j]] += 1
                j += 1
            
            subarr_len = j - i
            res = max(res, subarr_len)
                
        return res

if __name__ == "__main__":
    arr = [1, 4, 4, 3]
    k = 1

    print(Solution().maxSubarrayLength(arr, k))
