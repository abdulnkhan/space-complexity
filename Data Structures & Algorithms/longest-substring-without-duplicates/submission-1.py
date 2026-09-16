class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
            - Use set
            - Initialize res = 0 
            - 2 pointers - lp = 0 and rp goes through all values
            - Cycle through rp and check if rp already exists in set 
                - If yes reduce the window from left with set.remove(s[lp])
            - Add rp val after this
            - Calculate res by using max function with rp - lp + 1
        """
        charSet = set()
        result = 0
        lp = 0

        for rp in range(len(s)):
            while s[rp] in charSet:
                charSet.remove(s[lp])
                lp += 1
            charSet.add(s[rp])
            result = max(result, rp - lp + 1)
        
        return result
