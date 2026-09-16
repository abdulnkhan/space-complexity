class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in res.keys():
                return [res[diff], i]
            else:
                res[num] = i
        
        return False