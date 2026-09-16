class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCount = {}

        for word in strs:
            chars = [0] * 26

            for i in word:
                pos = ord(i) - ord('a')
                chars[pos] += 1

            key = tuple(chars)
            
            if key in charCount.keys():
                charCount[key].append(word)
            else:
                charCount[key] = [word]

        return list(charCount.values())