# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
            - Declare dummy node thats at the beginning of the list
            - The LP will start at the dummy node
            - Right pointer will start at head and r++ until at n position
            - At this point LP is at dummy node & RP is at n-th position
                - keep doing a while loop until the RP is None
            - Once RP is None -> I know LP is at the node behind the one we want to delete
                - left.next.next
            - return dummy.next
        """
        dummy = ListNode(0, head)
        lp = dummy
        rp = head

        j = 0
        while j < n:
            rp = rp.next
            j += 1

        while rp:
            lp = lp.next
            rp = rp.next

        # Delete the node now
        lp.next = lp.next.next

        return dummy.next

            