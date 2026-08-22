# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        """
        Recursive pre-order DFS solution

        Time: O(n)
        Space: O(h), height of the tree (worst case O(n) for unbalance trees)
        """
        self.flag = False

        def dfs(node: TreeNode | None, cur_sum: int) -> None:
            if self.flag or node is None:
                return

            # add node's val to the current_sum
            cur_sum += node.val

            # once we hit a leaf (no left and right child)
            # verify whether the path sum equals target
            if node.left is None and node.right is None:
                if cur_sum == targetSum:
                    self.flag = True
                    return

            dfs(node.left, cur_sum)
            dfs(node.right, cur_sum)
        
        dfs(root, 0)
        return self.flag
        