import heapq

"""
Maintain 2 heaps:
left side: max heap, right side: min heap

Key Invariant:
- Ensure left heap size at most 1 more than right heap
"""
class MedianFinder:

    def __init__(self):
        self.left = [] # max heap
        self.right = [] # min heap
        

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.left, num)
        left_max = heapq.heappop_max(self.left)
        heapq.heappush(self.right, left_max)

        # Maintain our invariant
        if len(self.left) < len(self.right):
            right_min = heapq.heappop(self.right)
            heapq.heappush_max(self.left, right_min)

    def findMedian(self) -> float:
        # even length
        if (len(self.left) + len(self.right)) % 2 == 0:
            return (self.left[0] + self.right[0]) / 2
        else: # odd length
            return self.left[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()