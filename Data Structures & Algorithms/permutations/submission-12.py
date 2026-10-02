class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()

        def backtrack(curr):
            if len(used) == len(nums):
                res.append(curr.copy())
                return

            for n in nums:
                if n in used:
                    continue

                used.add(n)
                curr.append(n)
                backtrack(curr)
                used.remove(n)
                curr.pop()

        backtrack([])
        return res