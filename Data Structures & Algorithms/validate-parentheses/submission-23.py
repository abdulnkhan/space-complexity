class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == ")" or s[0] == "}" or s[0] == "]":
            return False
        
        matchDict = {"}":"{", ")":"(", "]":"["}
        stack = []

        for i in range(len(s)):
            if s[i] in matchDict.keys():
                if len(stack) > 0 and matchDict[s[i]] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        return len(stack) == 0