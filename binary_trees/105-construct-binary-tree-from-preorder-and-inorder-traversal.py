# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """
        Divide and conquer solution, limit-based approach.

        pre_idx tells us which node to create next, 
        and in_idx tells us when we have finished a subtree.

        O(n) time
        O(n) space (recursion stack)
        """
        self.pre_idx, self.in_idx = 0, 0

        def build_subtree(limit: int | float) -> TreeNode | None:
            # all elements have been used
            if self.pre_idx == len(preorder):
                return None
            # the current subtree has reached its inorder boundary
            elif inorder[self.in_idx] == limit: 
                self.in_idx += 1
                return None

            root = TreeNode(preorder[self.pre_idx])
            self.pre_idx += 1

            root.left = build_subtree(root.val)
            root.right = build_subtree(limit)

            return root

        # run with an arbitary limit at first
        return build_subtree(float("inf"))

class Solution1:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """
        Divide and conquer solution,
        uses same approach as O(n^2) solution but we use 
        hash table to track indices in inorder as optimisation

        O(n) time
        O(n) space
        """
        inorder_indices = {
            val: idx for idx, val in enumerate(inorder)
        }

        self.pre_idx = 0

        # l and r track indices in inorder
        def build_subtree(l: int, r: int) -> TreeNode | None:
            if l > r:
                return None

            root = TreeNode(preorder[self.pre_idx])
            mid = inorder_indices[preorder[self.pre_idx]]
            self.pre_idx += 1

            root.left = build_subtree(l, mid - 1)
            root.right = build_subtree(mid + 1, r)

            return root

        return build_subtree(0, len(inorder) - 1)


class Solution2:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        """
        Divide and conquer method
        O(n^2) time
        O(n) space to store subarrays

        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]

        -> first element (3) in preorder is always the root
        preorder is at index mid (1) in inorder
        - All elements before index mid are in the left subtree 
        - thare are mid items in the left subtree, so preorder[1: mid + 1] are elements in the left subtree
        - remaining elements in the right subtree

        Recursively build left and right subtrees using the same logic
        """
        # Base case, break when both arrays empty
        if not preorder and not inorder:
            return 

        # Get root and find its index
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # there are mid elements in left subtree
        root.left = self.buildTree(
            preorder[1:mid + 1], 
            inorder[:mid]
        )

        # remaianing elements on right subtree
        root.right = self.buildTree(
            preorder[mid + 1:], 
            inorder[mid + 1:]
        )

        return root
