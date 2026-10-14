class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dictMap = {"}":"{", "]":"[", ")":"("}

        for i in range(len(s)):
            if s[i] in dictMap:
                if len(stack) > 0 and stack[-1] == dictMap[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        return True if len(stack) == 0 else False