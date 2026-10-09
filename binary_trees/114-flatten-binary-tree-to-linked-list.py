# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Morris Traversal (Iterative)
        O(n) time
        O(1) space
        """
        cur = root
        while cur is not None:
            # if we have a left subtree
            if cur.left is not None:
                # Go to rightmost node of left subtree
                tmp = cur.left
                while tmp.right is not None:
                    tmp = tmp.right

                # connect it to our right subtree
                tmp.right = cur.right
                # make left subtree our new right
                cur.right = cur.left

                # remember to set left subtree to None
                cur.left = None
            
            # Go to next child
            cur = cur.right

class Solution1:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Preorder traversal
        O(n) time
        O(h) space (recursion stack)
        """
        self.cur = None

        def preorder(root: TreeNode | None) -> None:
            if root is None:
                return

            # disconnect root from subtrees
            left, right = root.left, root.right
            root.left, root.right = None, None

            if self.cur is None:
                self.cur = root
            else:
                self.cur.right = root
                self.cur = self.cur.right

            preorder(left)
            preorder(right)

        preorder(root)

class Solution2:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Saving Preorder Traversal in List
        O(n) time
        O(n) space
        """
        if root is None:
            return None
        
        # build preorder list
        nodes = []
        def preorder(root: TreeNode | None) -> None:
            if root is None:
                return

            nodes.append(root)
            preorder(root.left)
            preorder(root.right)
        preorder(root)

        # use the preorder list to build the linked list
        nodes[0].left = None
        for i in range(1, len(nodes)):
            nodes[i].left = None
            nodes[i - 1].right = nodes[i]
        