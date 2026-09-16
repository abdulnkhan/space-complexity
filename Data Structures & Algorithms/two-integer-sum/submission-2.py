class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, num in enumerate(nums):
            comp = target - num
            if comp in numMap.keys():
                return [numMap[comp], i]
            else:
                numMap[num] = i
        return False