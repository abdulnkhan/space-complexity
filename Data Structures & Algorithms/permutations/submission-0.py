class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        def backtracking(curr):
            if len(used) == len(nums):
                res.append(curr.copy())
                return

            for n in nums:
                if n in used:
                    continue

                used.add(n)
                curr.append(n)

                backtracking(curr)

                curr.pop()
                used.remove(n)

        backtracking([])
        return res