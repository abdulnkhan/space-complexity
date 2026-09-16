class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)

        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            lp, rp = i + 1, len(nums) - 1

            while lp < rp:
                threeSum = num + nums[lp] + nums[rp]
                if threeSum > 0:
                    rp = rp - 1
                elif threeSum < 0:
                    lp = lp + 1
                else:
                    res.append([num, nums[lp], nums[rp]])
                    lp = lp + 1
                    rp = rp - 1
                    while lp < rp  and nums[lp] == nums[lp-1]:
                        lp = lp + 1
        return res
                
            