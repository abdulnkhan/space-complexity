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
        folders = path.split("/")

        for i in range(len(folders)-1):
            curr = curr.children[folders[i]]
            if curr.eof:
                return True
        return False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = TrieNode()

        for f in folder:
            root.add(f)

        res = []
        for f in folder:
            if not root.search(f):
                res.append(f)
        return res