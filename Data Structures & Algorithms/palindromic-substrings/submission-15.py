class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        for i in range(len(s)):
            # odd nums
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                r += 1
                l -= 1

            # even nums
            l = i
            r = l + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                r += 1
                l -= 1

        return count
