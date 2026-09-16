class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            lp = i + 1
            rp = len(nums) - 1

            while lp < rp:
                if nums[i] + nums[lp] + nums[rp] > 0:
                    rp -= 1
                elif nums[i] + nums[lp] + nums[rp] < 0:
                    lp += 1
                else:
                    res.append([nums[i], nums[lp], nums[rp]])
                    lp += 1
                    rp -= 1
                    while lp < rp and nums[lp] == nums[lp-1]:
                        lp += 1

        return res