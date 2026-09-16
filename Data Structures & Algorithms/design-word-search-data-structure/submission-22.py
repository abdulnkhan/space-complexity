class TrieNode:
    def __init__(self):
        self.children = {}
        self.eof = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in word:
            if i not in curr.children.keys():
                curr.children[i] = TrieNode()
            curr = curr.children[i]

        curr.eof = True

    def search(self, word: str) -> bool:
        self.word = word
        return self.dfs(0, self.root)

    def dfs(self, j, curr):
        word = self.word

        for i in range(j, len(word)):
            if word[i] == ".":
                for child in curr.children.values():
                    if self.dfs(i+1, child):
                        return True
                return False
            elif word[i] not in curr.children.keys():
                return False
            else:
                curr = curr.children[word[i]]

        return curr.eof
