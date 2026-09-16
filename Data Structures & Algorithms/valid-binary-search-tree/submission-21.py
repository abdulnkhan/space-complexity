# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValid(root, float("-inf"), float("+inf"))

    def isValid(self, curr, left, right):
        if not curr:
            return True

        if not (left < curr.val < right):
            return False

        return self.isValid(curr.left, left, curr.val) and self.isValid(curr.right,curr.val,right)