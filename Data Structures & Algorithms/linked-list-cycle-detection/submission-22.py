# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
            seen = {}

            curr = head
            i = 0
            while curr:
                if curr in seen:
                    return True
                seen[curr] = i
                curr = curr.next
        """
        curr = head
        seen = {}
        i = 0

        while curr:
            if curr in seen.values():
                return True
            seen[i] = curr
            i += 1
            curr = curr.next
        return False
