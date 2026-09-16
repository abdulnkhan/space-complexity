class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        result = 0

        lp = 0

        for rp in range(len(s)):
            while s[rp] in charSet:
                charSet.remove(s[lp])
                lp += 1
            charSet.add(s[rp])

            result = max(result, rp - lp +1)
        return result