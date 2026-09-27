from collections import deque

#  Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        O(n) time and O(1) space
        """
        if root is None:
            return

        cur = root

        while cur is not None: 
            dummy = Node()
            tail = dummy # tracks last node in next level

            # Traverse current level using next pointers
            while cur is not None:
                # Connect nodes in the next level
                if cur.left is not None:
                    tail.next = cur.left
                    tail = tail.next

                if cur.right is not None:
                    tail.next = cur.right
                    tail = tail.next

                # Next node in first level
                cur = cur.next
            
            # first node in the next level
            cur = dummy.next

        return root

    def connect2(self, root: 'Node') -> 'Node':
        """
        Level-order traversal
        O(n) time and space
        """
        if root is None:
            return

        q = deque([root])
        while q:   
            prev = None

            for _ in range(len(q)):
                cur = q.popleft()

                if prev is not None:
                    prev.next = cur

                for child in (cur.left, cur.right):
                    if child is not None:
                        q.append(child)

                prev = cur

        return root