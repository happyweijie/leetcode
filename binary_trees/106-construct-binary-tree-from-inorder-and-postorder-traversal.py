# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    """
    Mirror image of LC 105 
    """    
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        """
        Divide and Conquer using limit
        O(n) algorithm
        O(n) space for recursive stack
        """
        self.post_idx = len(postorder) - 1
        self.in_idx = len(postorder) - 1

        # l and r tracks index in inorder
        def dfs(limit: float | int) -> TreeNode | None:
            if self.post_idx < 0:
                return None
            elif inorder[self.in_idx] == limit:
                self.in_idx -= 1
                return None

            root = TreeNode(postorder[self.post_idx])
            self.post_idx -= 1

            root.right = dfs(root.val)
            root.left = dfs(limit)

            return root

        return dfs(float("inf"))

    def buildTree1(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        """
        Divide and Conquer: use dictionary to track inorder indices
        O(n) algorithm
        O(n) space
        """
        # hash map to track inorder index
        inorder_indices = {val: idx for idx, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        # l and r tracks index in inorder
        def dfs(l: int, r: int) -> TreeNode | None:
            if l > r:
                return None

            root = TreeNode(postorder[self.post_idx])
            self.post_idx -= 1

            root.right = dfs(inorder_indices[root.val] + 1, r)
            root.left = dfs(l, inorder_indices[root.val] - 1)

            return root

        return dfs(0, len(inorder) - 1)

    def buildTree2(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        """
        Divide and Conquer
        O(n^2) algorithm
        O(n) space
        """
        if not inorder and not postorder:
            return None
        else:
            n = len(inorder) 
            root = TreeNode(postorder[n - 1]) 
            mid = inorder.index(root.val) 
            right_subtree_size = n  - 1 - mid

            root.right = self.buildTree(
                inorder[mid + 1:],
                postorder[n - 1 - right_subtree_size:n - 1],
            )
            root.left = self.buildTree(
                inorder[:mid],
                postorder[:n - 1 - right_subtree_size]
            )

            return root
