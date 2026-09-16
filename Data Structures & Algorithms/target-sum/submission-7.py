class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtracking(i, curr_sum):
            if len(nums) == i:
                if target == curr_sum:
                    return 1
                else:
                    return 0

            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]

            memo[(i, curr_sum)] = (backtracking(i+1, curr_sum + nums[i]) + backtracking(i+1, curr_sum - nums[i]))
            return memo[(i, curr_sum)]

        return backtracking(0,0)