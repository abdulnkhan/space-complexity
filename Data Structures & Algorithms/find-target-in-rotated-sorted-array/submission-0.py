class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            mp = (rp + lp) // 2
            if target == nums[mp]:
                return mp

            if nums[lp] <= nums[mp]: #left half is sorted
                if nums[lp] <= target < nums[mp]:
                    rp = mp -1
                else:
                    lp = mp + 1

            else: # right half is sorted nums[mp] target nums[rp]
                if nums[mp] < target <= nums[rp]:
                    lp = mp + 1
                else:
                    rp = mp -1

        return -1


