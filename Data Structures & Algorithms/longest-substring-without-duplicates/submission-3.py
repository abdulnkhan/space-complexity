class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        lp = 0 
        res = 0

        for rp in range(len(s)):
            while s[rp] in charSet:
                charSet.remove(s[lp])
                lp = lp + 1
            charSet.add(s[rp])
            res = max(res, rp - lp + 1)
        return res