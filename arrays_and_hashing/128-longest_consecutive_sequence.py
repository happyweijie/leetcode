class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        array is unsorted, can sort but it will be o(n log n)
        ignore duplicates => [1,0,1,2] -> only 0,1,2

        Time complexity: O(n)
        Space complexity: O(n)
        """
        unique_nums = set(nums) # use a set to remove duplicates

        res = 0
        # just iterate over the set instead of the list
        for n in unique_nums:
            # don't care about elements already
            # in some sequence
            if n - 1 in unique_nums:
                continue

            # we found the start of a new sequence
            cur_len = 1
            succ = n + 1
            while succ in unique_nums:
                cur_len += 1
                succ += 1

            res = max(res, cur_len)

        return res

    def longestConsecutiveUFDS(self, nums: list[int]) -> int:
        unique_nums = set(nums) # use a set to remove duplicates
        ufds = UFDS(unique_nums)
        res = 0

        for n in unique_nums:
            if n - 1 in unique_nums:
                ufds.union(n, n - 1)

            if n + 1 in unique_nums:
                ufds.union(n, n + 1)

            res = max(res, ufds.get_size(n))

        return res


class UFDS:
    def __init__(self, nums):
        self.parent = {n: n for n in nums}
        # use union by size since we need size anyways
        self.size = {n: 1 for n in nums}

    def find(self, u):
        if self.parent[u] == u:
            return u

        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        # parent of u and v
        x, y = self.find(u), self.find(v)

        # do nothing if u and v are in same set already
        if x == y:
            return

        # union by size: make the smaller tree the child of larger subtree
        if self.size[x] > self.size[y]:
            self.parent[y] = x
            self.size[x] += self.size[y]
        else: # size[x] ]<= size[y]
            self.parent[x] = y
            self.size[y] += self.size[x]

    def get_size(self, u):
        return self.size[self.find(u)]
