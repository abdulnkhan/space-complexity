class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        char_count = {}
        
        for word in strs:
            chars = [0] * 26

            for i in word:
                pos = ord(i) - ord('a')
                chars[pos] += 1

            key = tuple(chars)
            
            if key in char_count.keys():
                char_count[key].append(word)
            else:
                char_count[key] = [word]

        return list(char_count.values())
                