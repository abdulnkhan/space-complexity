# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        - Declare dummy node -> lp will be initialzed here
        - Declare rp -> start at head -> move rp to nth position
        - Then move both lp and rp together until rp is None - we know lp will be at the node before remove
        - Just move lp twice
        """

        dummy = ListNode(0,head)
        lp = dummy
        rp = head

        i = 0

        while i < n:
            rp = rp.next
            i += 1

        while rp:
            lp = lp.next
            rp = rp.next

        lp.next = lp.next.next

        return dummy.next
