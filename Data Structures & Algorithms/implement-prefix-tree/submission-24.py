class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for i in word:
            if i not in curr.children.keys():
                curr.children[i] = TrieNode()
            curr = curr.children[i]

        curr.eow = True

    def search(self, word: str) -> bool:
        curr = self.root

        for i in word:
            if i not in curr.children.keys():
                return False
            curr = curr.children[i]

        return curr.eow

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for i in prefix:
            if i not in curr.children.keys():
                return False
            curr = curr.children[i]

        return True
        