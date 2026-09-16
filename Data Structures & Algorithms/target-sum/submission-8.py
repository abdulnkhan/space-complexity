class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def backtrack(i, curr_sum):
            if i == len(nums):
                if target == curr_sum:
                    return 1
                else:
                    return 0


            memo[(i, curr_sum)] = (backtrack(i+1, curr_sum+nums[i]) +
                                   backtrack(i+1, curr_sum-nums[i]))
            
            return memo[(i, curr_sum)]

        return backtrack(0,0)