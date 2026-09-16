class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charCount = {}

        for word in strs:
            charFreq = [0] * 26
            for i in word:
                spot = ord('a') - ord(i)
                charFreq[spot] += 1

            pos = tuple(charFreq)
            if pos in charCount:
                charCount[pos].append(word)
            else:
                charCount[pos] = [word]

        return list(charCount.values())


            