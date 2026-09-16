class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = set()
        lp = 0
        res = 0

        for rp in range(len(s)):
            while s[rp] in char:
                char.remove(s[lp])
                lp += 1
            char.add(s[rp])
            res = max(res ,rp - lp + 1)

        return res