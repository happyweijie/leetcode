from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        Using dictionary to store each node's copy

        Time: O(n)
        Space: O(1) excluding space for copy list
        """
        if head is None:
            return head

        # First copy the main list first
        cur = head

        # interleave each node with its copy
        # Old List: A --> B --> C
        # InterWeaved List: A --> A' --> B --> B' --> C --> C'
        while cur is not None:
            nxt = cur.next

            # interweave
            cur_prime = Node(cur.val)
            cur.next = cur_prime
            cur_prime.next = nxt

            cur = cur.next.next
        
        # remember to set cur back to head
        cur = head
        res = Node(-999999)
        res_cur = res

        while cur is not None:
            # copy the random pointer to cur_prime
            cur_prime = cur.next
            if cur.random is not None:
                cur_prime.random = cur.random.next

            # set cur to next original node
            cur = cur.next.next

            # move the copy node to result list
            cur_prime.next = None
            res_cur.next = cur_prime
            res_cur = res_cur.next

        return res.next

        """
        Note: this algorithm mutates the original list
        To properly maintain the original list, we need 3 while loops:
        first for interleaving
        second for copying random pointer
        third for separating the two lists

        Random pointers can point backwards so it is not
        safe to separate the two lists in the second loop
        """

    def copyRandomList2(self, head: Optional[Node]) -> Optional[Node]:
        """
        Using dictionary to store each node's copy

        Time: O(n)
        Space: O(n) excluding space for copy list
        """
        if head is None:
            return head

        # maps original node to its copy
        copy: dict[Node, Node] = {}

        # First copy the main list first
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
