import heapq

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        pq = []

        for x, y in points:
            # Use max heap instead of min heap
            # if we use min heap, heappop would remove
            # the smallest element, if we exceed k
            # we shld remove the k+1 th element
            heapq.heappush_max(pq, ((x ** 2 + y ** 2), [x, y]))

            if len(pq) > k:
                heapq.heappop_max(pq)       

        return [pt for _, pt in pq]