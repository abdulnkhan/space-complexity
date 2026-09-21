"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodeCopy = {}

        def dfs(node):
            """
            check if node already exists
                if yes return nodeCopy[node]
            
            create copy node

            for neigh in node.neighbors:
                copy node.neighbors.append(dfs(neigh))

            """
            if node in nodeCopy:
                return nodeCopy[node]

            copy = Node(node.val)
            nodeCopy[node] = copy

            for neigh in node.neighbors:
                copy.neighbors.append(dfs(neigh))

            return copy

        return dfs(node)
        