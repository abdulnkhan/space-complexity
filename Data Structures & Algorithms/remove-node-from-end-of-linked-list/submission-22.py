# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        dummy = ListNode(0, head)
        dummy -> list

        lp = dummy
        rp = dummy.next

        i = 0
        while i <= n:

        """

        dummy = ListNode(0, head)
        lp = dummy
        rp = dummy.next

        i = 0
        while i < n:
            rp = rp.next
            i += 1

        while rp:
            lp = lp.next
            rp = rp.next

        lp.next = lp.next.next

        return dummy.next