class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
            my exit condition is when i == len(nums) - this is because I know at this point i have already gone through the whole array - if i see i >= len(nums) then i have exceeded my condition and just need to return
            first i'll add the current element and +1 on i to keep that chain going
            then i pop it add call backtracking again basically skipping that element
        """

        res = []

        def backtrack(i, curr):
            if i == len(nums):
                res.append(curr.copy())
                return
            if i >= len(nums):
                return

            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
            backtrack(i+1, curr)

        backtrack(0,[])

        return res