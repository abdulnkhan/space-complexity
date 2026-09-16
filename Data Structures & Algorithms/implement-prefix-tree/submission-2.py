class TreeNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for i in word:
            if i not in curr.children:
                curr.children[i] = TreeNode()
            curr = curr.children[i]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root

        for i in word:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for i in prefix:
            if i not in curr.children:
                return False
            curr = curr.children[i]
        return True
        