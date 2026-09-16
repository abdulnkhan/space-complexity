# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
            dummy ListNode() -> head
            second -> head
            first = dummy
            first to be one before the node i want to get rid of 
            and do first.next = first.next.next

            i = 0 because i'll iterate at the beginning
        """

        dummy = ListNode(0, head)
        first = dummy
        second = head

        i = 0
        while i < n:
            second = second.next
            i += 1

        while second:
            first = first.next
            second = second.next

        first.next = first.next.next

        return dummy.next