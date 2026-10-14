class Solution:
    def search(self, nums: List[int], target: int) -> int:
            lp = 0
            rp = len(nums) - 1

            while lp <= rp:
                mp = rp - (rp - lp) // 2

                if nums[mp] == target:
                    return mp

                if nums[lp] <= nums[mp]: # left half is sorted
                    if nums[lp] <= target < nums[mp]:
                        rp = mp - 1 # exists before mp 
                    else:
                        lp = mp + 1 # exists after mp

                else:
                    if nums[mp] < target <= nums[rp]:
                        lp = mp + 1
                    else:
                        rp = mp - 1

            return -1
