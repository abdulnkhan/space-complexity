class Solution:
    def isValid(self, s: str) -> bool:
        if s[0] == '}' or s[0] == ']' or s[0] == ')':
            return False
        stack = []
        match = {")": "(", "}": "{", "]":"["}

        for i in range(len(s)):
            if s[i] in match.keys():
                if len(stack) > 0 and stack[-1] == match[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return stack == []
        