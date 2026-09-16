class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCount = {}
        res = 0
        lp = 0

        for rp in range(len(s)):
            charCount[s[rp]] = 1 + charCount.get(s[rp], 0)

            while (rp - lp + 1) - max(charCount.values()) > k:
                charCount[s[lp]] -= 1
                lp += 1

            res = max(res, rp - lp + 1)
        return res
    