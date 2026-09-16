class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            char = [0] * 26
            for i in word:
                pos = ord(i) - ord('a')
                char[pos] += 1
            key = tuple(char)
            if key in res.keys():
                res[key].append(word)
            else:
                res[key] = [word]

        return list(res.values())                