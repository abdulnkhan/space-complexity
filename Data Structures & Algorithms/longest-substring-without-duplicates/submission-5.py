class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 
        In this we iterate through the each element in the array and initialze lp as 0 - each time we find a duplicate we reduce window size from the left by increasing lp - after this we just add s[rp] to the charSet and calculate if res is now more than before with max function
        """
        charSet = set()
        lp = 0
        res = 0

        for rp in range(len(s)):
            while s[rp] in charSet:
                charSet.remove(s[lp])
                lp += 1
            charSet.add(s[rp])
            res = max(res, rp - lp + 1)

        return res