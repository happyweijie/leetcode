
from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Using dictionary to store each node's copy

        Time: O(n)
        Space: O(n), storing each node's copy in a dictionary
        """
        if head is None:
            return head

        # maps original nodes to their copies
        copy: dict[Node, Node] = {}

        # First copy the list first
        cur = head

        cpy_res =  Node(-9999)
        cpy_cur = cpy_res

        while cur is not None:
            copy[cur] = Node(cur.val)
            cpy_cur.next = copy[cur]

            cur = cur.next
            cpy_cur = cpy_cur.next
        
        # Then copy over the random pointers
        cur = head
        cpy_res = cpy_res.next
        cpy_cur = cpy_res

        while cur is not None:
            if cur.random is not None:
                cpy_cur.random = copy[cur.random]

            cur = cur.next
            cpy_cur = cpy_cur.next

        return cpy_res
