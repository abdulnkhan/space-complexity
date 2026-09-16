class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCount = {}
        for word in strs:
            charList = [0] * 26
            for i in word:
                pos = ord(i) - ord('a')
                charList[pos] += 1
            key = tuple(charList)
            if key in charCount:
                charCount[key].append(word)
            else:
                charCount[key] = [word]

        return list(charCount.values())


            