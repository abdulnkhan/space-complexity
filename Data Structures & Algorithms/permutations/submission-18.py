class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        we're going to use a used set and keep cycling through until all used are added to the result then we will return

        are we worried about duplicates? if no then we dont have run the loop with indices otherwise we do
        """
        
        res = []
        used = set()

        def backtrack(curr):
            if len(used) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if nums[i] in used:
                    continue

                curr.append(nums[i])
                used.add(nums[i])
                backtrack(curr)
                curr.pop()
                used.remove(nums[i])

        backtrack([])
        return res