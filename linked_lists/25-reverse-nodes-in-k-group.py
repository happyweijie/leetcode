# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode | None, k: int) -> ListNode | None:
        """
        Time complexity: O(n), where n is the number of nodes in the linked list.
        Space complexity: O(1), since we are reversing the nodes in place.

        Note: Recursive reversal uses O(k) space for recursive calls.
        """
        if head is None:
            return head

        res = ListNode()
        res_cur = res

        cur = head
        while cur:
            grp_len = 1
            
            start, end = cur, cur
            for _ in range(k - 1):
                end = end.next

                if end is None:
                    break

                grp_len += 1
            
            # don't reverse if group length < k
            if grp_len != k:
                res_cur.next = start
                break

            tmp = end.next
            end.next = None

            # reverse grp
            self.reverse_group(start)

            # connect reversed list to result
            res_cur.next = end
            res_cur = start

            cur = tmp

        return res.next

    def reverse_group(self, node: ListNode) -> None:
        res = ListNode()

        while node:
            # detach node from the list
            nxt = node.next
            node.next = None

            # insert node at the beginning of the reversed list
            node.next = res.next
            res.next = node

            node = nxt

        return res.next
    