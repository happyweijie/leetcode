class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        """
        Monotonic Stack approach

        Time complexity: O(n)
        Space complexity: O(n)
        """
        answer = [0] * len(temperatures)

        # The stack stores (temp, idx)
        # montonic decreasing stack (temperatures must be smaller and smaller)
        stack = [(temperatures[0], 0)]

        for i in range(1, len(temperatures)):

            # keep popping all temperatures lower than current temp
            # updating the day accordingly            
            while stack and temperatures[i] > stack[-1][0]:
                _, day = stack[-1]

                answer[day] = i - day
                stack.pop()

            stack.append((temperatures[i], i))

        return answer