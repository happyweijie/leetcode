from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        """
        Level-Order Traversal (BFS)
        Time: O(n)
        Space: O(n)
        """
        if root is None:
            return []

        res = []
        q = deque([root])

        while q:
            # track last elemenet in the current level
            last = None

            for _ in range(len(q)):
                cur = q.popleft()
                last = cur.val

                for child in (cur.left, cur.right):
                    if child is not None:
                        q.append(child)

            res.append(last)

        return res
    