# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}
        i = 0
        curr = head

        while curr:
            if curr in seen.values():
                return True
            else:
                seen[i] = curr
                i += 1
                curr = curr.next
        return False
