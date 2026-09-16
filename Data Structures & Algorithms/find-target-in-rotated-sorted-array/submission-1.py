class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            - two points with condition lp <= rp 
            - calc mp - if target == val[mp] return mp
            - If lp < mp - we know left half is sorted
                - lp <= val < mp so move accordingly
            - otherwise we are going to check the right half
                - mp < val <= rp
            - remember mp is not = because we check this earlier

        """
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            mp = (lp + rp) // 2
            if target == nums[mp]:
                return mp

            if nums[lp] <= nums[mp]: #left half is sorted
                if nums[lp] <= target < nums[mp]:
                    rp = mp - 1
                else: 
                    lp = mp + 1
            else: #mp target rp
                if nums[mp] < target <= nums[rp]:
                    lp = mp + 1
                else: 
                    rp = mp -1
        return -1
