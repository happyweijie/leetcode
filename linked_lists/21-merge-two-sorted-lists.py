from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merge two sorted linked lists similar to
        merge in merge sort.

        Time: O(n + m) where n and m are the lengths of the two lists.
        Space: O(1)
        """
        res = ListNode()
        cur = res

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                tmp = list1
                list1 = list1.next
            else:
                tmp = list2
                list2 = list2.next

            tmp.next = None
            cur.next = tmp
            cur = cur.next

        if list1 is not None:
            cur.next = list1
        
        if list2 is not None:
            cur.next = list2
            
        return res.next
        