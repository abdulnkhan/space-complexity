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
        copyNode dict: maps old to new nodes
        then i do a simple dfs and create a new node if its there otherwise copy over and call dfs inside that
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