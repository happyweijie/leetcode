# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        """
        Time: O(n)
        Space: O(1)
        """
        if head is None:
            return head

        left = ListNode() # stores values < x
        left_cur = left
        right = ListNode() # stores values >= x
        right_cur = right

        cur = head
        while cur is not None:
            tmp = cur.next
            cur.next = None

            if cur.val < x:
                left_cur.next = cur
                left_cur = left_cur.next
            else:
                right_cur.next = cur
                right_cur  = right_cur.next

            cur = tmp

        # connect the two lists
        left_cur.next = right.next
        return left.next
