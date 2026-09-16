class Solution:
    def findMin(self, nums: List[int]) -> int:
        lp = 0
        rp = len(nums)-1

        while lp < rp:
            mp = (rp + lp) // 2

            if nums[mp] > nums[rp]:
                lp = mp + 1
            else: 
                rp = mp 
        return nums[lp]