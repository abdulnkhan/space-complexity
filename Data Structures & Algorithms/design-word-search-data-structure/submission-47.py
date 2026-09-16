class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for i in word:
            if i not in curr.children:
                curr.children[i] = TrieNode()
            curr = curr.children[i]
        curr.eow = True

    def search(self, word: str) -> bool:

        def dfs(j, curr):
            for i in range(j, len(word)):
                if word[i] == ".":
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                    return False
                elif word[i] not in curr.children:
                    return False
                else:
                    curr = curr.children[word[i]]

            return curr.eow


        return dfs(0, self.root)