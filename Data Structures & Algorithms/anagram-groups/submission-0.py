class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCount = {}

        for word in strs:
            count = [0] * 26
            for i in word:
                count[ord(i) - ord("a")] += 1
            
            key = tuple(count)
            if key not in charCount.keys():
                charCount[key] = [word]
            else:
                charCount[key].append(word)

        return list(charCount.values())
