# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def isValid(left, curr, right):
            if not curr:
                return True

            if not (left < curr.val < right):
                return False

            return isValid(left, curr.left, curr.val) and isValid(curr.val, curr.right, right)

        return isValid(float("-inf"), root, float("+inf"))