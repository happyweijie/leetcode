from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: list[str]) -> int:
        bank = set(bank)
        if endGene not in bank:
            return -1

        # Use BFS to find the shortest path from startGene to endGene
        q, visited = deque([startGene]), set([startGene])
        steps = 0

        while q:
            steps += 1

            # all genes reachable in current step
            for _ in range(len(q)):
                cur = q.popleft()

                # Use the wildcard approach to find neighbors
                for i in range(len(cur)):
                    # replace index i with one of the chars
                    for char in ("A", "C", "G", "T"):
                        mutation = "".join([cur[:i], char, cur[i + 1:]])

                        if mutation in bank and mutation not in visited:
                            if mutation == endGene:
                                return steps

                            q.append(mutation)
                            visited.add(mutation)

        return -1
