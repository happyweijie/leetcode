class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        """
        Weighted Interval Scheduling (CS 341)

        Let n be number of jobs:
        Time: O(n log n)
        Space: O(n)
        """
        jobs = list(zip(startTime, endTime, profit))
        n = len(jobs)
        jobs.sort(key=lambda j: j[0]) # sort by start times
        
        # max profit we can get with i jobs
        # treat index n + 1 as amount from doing no jobs
        dp = [0] * (n + 1)
        
        # loop backwards
        # so job n is the first job and so on.
        for i in range(n - 1, -1, -1):
            # find next non-overlapping job
            nxt = self.binary_search_next(jobs, i + 1, n - 1, jobs[i][1])

            # recurrence
            # at job i, max we can earn is max of
            # 1. profit of job i + max we can earn from doing nxt to n-1 th job
            dp[i] = max(
                jobs[i][2] + (dp[nxt] if nxt != -1 else 0),
                dp[i + 1]
            )

        return dp[0]

    def binary_search_next(self, jobs: list[tuple], i: int, j: int, finish: int) -> int:
        while i <= j:
            mid = (i + j) // 2
            if jobs[mid][0] < finish:
                i = mid + 1
            elif jobs[mid][0] >= finish and jobs[mid - 1][0] >= finish:
                j = mid - 1 
            else:
                return mid

        return -1
    