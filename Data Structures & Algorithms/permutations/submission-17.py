class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visit = set()

        def backtrack(curr):
            if len(visit) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if i in visit:
                    continue
                
                visit.add(i)
                curr.append(nums[i])
                backtrack(curr)
                visit.remove(i)
                curr.pop()


        backtrack([])
        return res