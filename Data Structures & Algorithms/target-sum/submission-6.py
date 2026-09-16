class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtracking(i, curr_sum):
            if len(nums) == i:
                if target == curr_sum:
                    return 1
                else:
                    return 0

            return (backtracking(i+1, curr_sum + nums[i]) + backtracking(i+1, curr_sum - nums[i]))

        return backtracking(0,0)