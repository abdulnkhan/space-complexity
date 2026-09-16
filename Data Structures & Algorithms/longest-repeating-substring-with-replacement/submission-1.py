class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            - declare hashmap to check most repeating character 
            - declare res = 0
            - lp = 0 and rp with for loop
            - check if window is not valid with (rp - lp + 1) - max(charCount.values()) > k
                - if window is not valid -> charCount[s[lp]] -= 1 -> lp += 1
            - make sure res is updated with res = max(res, rp-lp+1)
        """
        charCount = {}
        res = 0 
        lp = 0

        for rp in range(len(s)):
            if s[rp] in charCount.keys():
                charCount[s[rp]] += 1
            else: 
                charCount[s[rp]] = 1
        
            while (rp - lp + 1) - max(charCount.values()) > k:
                charCount[s[lp]] -= 1
                lp += 1

            res = max(res, rp - lp + 1)
        return res
        
