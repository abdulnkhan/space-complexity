class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i in range(len(nums)):
            search = target - nums[i]

            if search in numMap:
                return [numMap[search], i]

            else:
                numMap[nums[i]] = i

        return False