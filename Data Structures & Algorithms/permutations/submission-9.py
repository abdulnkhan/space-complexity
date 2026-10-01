class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = set()

        def backtrack(curr):
            if len(visit) == len(nums):
                res.append(curr.copy())
                return

            for n in nums:
                if n in visit:
                    continue
                visit.add(n)
                curr.append(n)
                backtrack(curr)
                visit.remove(n)
                curr.pop()

        backtrack([])
        return res