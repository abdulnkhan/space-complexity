# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
            seen = {index: item}
            cycle through list and each time check if current item is in values()
                - if yes return True

            else return False
        """
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