class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(i, curr_sum):
            if i == len(nums):
                if curr_sum == target:
                    return 1
                else:
                    return 0

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            memo[(i, curr_sum)] = (backtrack(i+1, curr_sum+nums[i])) + (backtrack(i+1, curr_sum-nums[i]))

            return memo[(i, curr_sum)]



        return backtrack(0,0)