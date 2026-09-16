class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == "}" or s[0] == ")" or s[0] == "}":
            return False
        stack = []
        matcher = {")":"(", "}":"{", "]":"["}

        for i in range(len(s)):
            if s[i] in matcher.keys():
                if len(stack) > 0 and stack[-1] == matcher[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])

        return len(stack) == 0