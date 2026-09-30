class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        For this i'm going to have used set and a res array - the idea is i'm going to cycle through each num with a for loop and then backtrack while using the used set to make sure that element hasn't been used before to get all permutations
        """

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


