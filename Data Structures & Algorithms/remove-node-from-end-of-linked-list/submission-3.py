# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lp = dummy
        rp = head

        i = 0
        while i < n:
            rp = rp.next
            i = i + 1

        while rp:
            rp = rp.next
            lp = lp.next

        lp.next = lp.next.next

        return dummy.next

        