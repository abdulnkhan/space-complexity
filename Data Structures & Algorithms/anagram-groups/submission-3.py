class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            charCount = [0] * 26
            for i in word:
                pos = ord(i) - ord("a")
                charCount[pos] += 1
            key = tuple(charCount)

            if key in res.keys():
                res[key].append(word)
            else:
                res[key] = [word]
                

        return list(res.values())
            