"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        we will have dict that maps old node to the new node
        then we will do dfs to go through each of them -> check if in copyNode else create the new Node with val and also append the neighbors
        """
        if not node:
            return None
        copyNode = {}

        def dfs(node):
            if node in copyNode:
                return copyNode[node]

            copy = Node(node.val)
            copyNode[node] = copy

            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))

            return copy

        return dfs(node)