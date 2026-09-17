class Solution:
    def numDecodings(self, s: str) -> int:
        """
        '1221'

        Bottom up approach - dp
        dp = {len(s): 1}

        for i in range(len(s), -1, -1):
            if s[i]==0:
                dp[i] = 0 
            else: 
                dp[i] = dp[i+1] # We're taking one digit right here

            # Take 2 digits - we need to make sure it starts with 1 or 2 and 2nd digit it 0-6
            if s[i+1] < len(s) and (s[i] == 1 or (s[i] == 2 and s[i+1] in '0123456')
                dp[i] += dp[i+2]

        return dp[0]
        """
        
        dp = {len(s): 1}

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] = dp[i+1]

            #take 2nd digit, s + 1 < len(s) & (s[i]== 1 or (s[i] == 2 and s[i+1] in 0-6))
            if i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456')):
                dp[i] += dp[i+2]

        return dp[0]
