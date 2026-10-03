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
        self.in_idx = len(inorder) - 1

        def build_subtree(limit: float | int) -> TreeNode | None:
            # Scan inorder from right to left; limit marks the current subtree's boundary.
            if self.post_idx < 0:
                return None
            elif inorder[self.in_idx] == limit:
                self.in_idx -= 1
                return None

            root = TreeNode(postorder[self.post_idx])
            self.post_idx -= 1

            # Postorder is reversed: root, right subtree, then left subtree.
            root.right = build_subtree(root.val)
            root.left = build_subtree(limit)

            return root

        return build_subtree(float("inf"))

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
        def build_subtree(l: int, r: int) -> TreeNode | None:
            if l > r:
                return None

            root = TreeNode(postorder[self.post_idx])
            self.post_idx -= 1

            root.right = build_subtree(inorder_indices[root.val] + 1, r)
            root.left = build_subtree(l, inorder_indices[root.val] - 1)

            return root

        return build_subtree(0, len(inorder) - 1)

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

            root.right = self.buildTree2(
                inorder[mid + 1:],
                postorder[n - 1 - right_subtree_size:n - 1],
            )
            root.left = self.buildTree2(
                inorder[:mid],
                postorder[:n - 1 - right_subtree_size]
            )

            return root
