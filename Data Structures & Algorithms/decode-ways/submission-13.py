class Solution:
    def numDecodings(self, s: str) -> int:
        """
        In decode message I will start at the end of the string -> at each level i will decide if i'm going to take one digit or two digits. The safety check is if there is a 0 then i return 0

        dp = {len(s): 1}
        """
        dp = {len(s):1}
        
        for i in range(len(s)-1,-1,-1):
            if s[i] == '0':
                dp[i] = 0
            else: # Take one digit
                dp[i] = dp[i+1]

            # Take 2 digits
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                dp[i] += dp[i+2]

        return dp[0]