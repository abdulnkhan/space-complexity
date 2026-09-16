class TrieNode:
    def __init__(self):
        self.children = {}
        self.eof = False

    def add(self, path):
        curr = self
        for i in path.split("/"):
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.eof = True

    def search(self, path):
        curr = self
        folder = path.split("/")

        for i in range(len(folder)-1):
            curr = curr.children[folder[i]]
            if curr.eof:
                return False
        return True




class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()

        for f in folder:
            root.add(f)

        res = []

        for f in folder:
            if root.search(f):
                res.append(f)

        return res