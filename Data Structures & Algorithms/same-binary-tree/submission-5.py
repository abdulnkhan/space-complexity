# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        pq = deque([p])
        qq = deque([q])

        while pq and qq:
            n1 = pq.popleft()
            n2 = qq.popleft()

            if not n1 and not n2:
                continue
 
            if n1 and not n2:
                return False
            if n2 and not n1:
                return False
            if n1.val != n2.val:
                return False       


            pq.append(n1.left)
            qq.append(n2.left)
            pq.append(n1.right)
            qq.append(n2.right)
        
        return len(pq) == 0 and len(qq) == 0

        """
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            node1 = q1.popleft()
            node2 = q2.popleft()

            if node1 is None and node2 is None:
                continue

            if node1 is None and node2 is not None:
                return False
            if node2 is None and node1 is not None:
                return False
            if node1.val != node2.val:
                return False
            q1.append(node1.left)
            q1.append(node1.right)
            q2.append(node2.left)
            q2.append(node2.right)
    
        return len(q1) == 0 and len(q2) == 0

        """