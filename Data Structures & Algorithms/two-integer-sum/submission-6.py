class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            numArray = {num:pos}
            req = target - curr

            is req in numArray?
                - if yes, return indices
                - if no, lets add current item to numArray
        """

        numArray = {}

        for i, num in enumerate(nums):
            req = target - num

            if req in numArray.keys():
                return [numArray[req], i]
            else:
                numArray[num] = i
                
        return False