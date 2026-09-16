class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matchDict = {"}":"{", ")":"(", "]":"["}
        if s[0] == ")" or s[0] == "]" or s[0] == "}":
            return False
        for i in range(len(s)):
            if s[i] in matchDict:
                if len(stack) > 0 and stack[-1] == matchDict[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if stack == []:
            return True
        else:
            return False