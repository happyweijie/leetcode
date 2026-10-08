# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        """
        Time: O(n)
        Space: O(1)
        """
        if head is None:
            return None

        res = ListNode()
        res_cur = res

        cur = head
        while cur is not None:
            nxt: ListNode | None = cur.next
            if nxt is None:
                res_cur.next = cur
                break

            # save element after pair
            tmp = nxt.next

            # Swap cur and nxt
            nxt.next = cur
            cur.next = None

            # conect swapped pair to result
            res_cur.next = nxt
            # since cur and nxt are swapped, 
            # cur is now the last element in the pair
            res_cur = cur 

            cur = tmp
            
        return res.next
