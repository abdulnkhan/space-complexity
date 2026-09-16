# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = {}

        curr = head
        index = 0

        while curr:
            if curr in seen.values():
                return True
            else:
                seen[index] = curr
                index += 1

            curr = curr.next
        return False