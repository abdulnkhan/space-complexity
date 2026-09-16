class TrieNode:
    def __init__(self):
        self.children = {}
        self.eof = False

    def add(self, folder):
        curr = self
        for f in folder.split("/"):
            if f not in curr.children:
                curr.children[f] = TrieNode()
            curr = curr.children[f]
        curr.eof = True

    def search(self, folder):
        curr = self
        folders = folder.split("/")
        for f in range(len(folders)-1):
            curr = curr.children[folders[f]]
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