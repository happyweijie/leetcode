# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        """
        Divide and conquer approach.
        
        Recurrence: T(k) = T(k/2) + n = T(k/2) + k^(log n)
        Time: O(n log k)
        Space: O(log k) for recursion stack
        """
        k = len(lists)
        if k == 0:
            return None
        elif k == 1:
            return lists[0]

        # merge half of the lists at a time
        merged = []
        for i in range(0, k - 1, 2):
            merged.append(self.mergeTwoLists(lists[i], lists[i + 1]))

        # if there is an odd number of lists, add the last one
        if k % 2 == 1 and lists[k-1] is not None:
            merged.append(lists[k-1])

        # merge the merged lists recursively
        return self.mergeKLists(merged)
        

    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        """
        Same as 21-merge-two-sorted-lists

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
        