class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dp = [False] * (len(s) + 1) # sets up base case
        dp[len(s)] = True # base case is true

        for i in range(len(s)-1, -1,-1): # Moving backwards in DP array
            for w in word: # now we will actually check if each word is there
                if i + len(w) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i+len(w)]

                if dp[i]:
                    break
        return dp[0]
        """

        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if i+len(w) <= len(s) and s[i: i+len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break

        return dp[0]