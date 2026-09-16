# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
            - Declare curr = root -> then we basically want to traverse left or right
            - if p > curr and q > curr: # we know that its on the right side
            - elif p < curr and q < curr: # we know that its on the left side
            - else: p is on one side and q is on the other # we know that this is where the split happens
        """

        curr = root

        while curr: #okay to execute infinitely
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr