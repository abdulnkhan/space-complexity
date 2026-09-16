class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCount = {}

        for word in strs:
            char = [0] * 26
            for i in word:
                pos = ord(i) - ord('a')
                char[pos] = char[pos]+1
            key = tuple(char)
            if key not in charCount.keys():
                charCount[key] = [word]
            else:
                charCount[key].append(word)
        
        return list(charCount.values())