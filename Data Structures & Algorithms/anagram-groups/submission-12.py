class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
            res = {}

            wordList = [0] * 26

            for alphabet in word:
                wordlist = [1 0 1 ...]
            tuple(wordlist)
            res[wordlist].append(word)
        """
        res = {}

        for word in strs:
            wordCount = [0] * 26 
            for i in word:
                pos = ord(i) - ord('a')
                wordCount[pos] += 1

            word_place = tuple(wordCount)

            if word_place in res.keys():
                res[word_place].append(word)
            else:
                res[word_place] = [word]

        return list(res.values())