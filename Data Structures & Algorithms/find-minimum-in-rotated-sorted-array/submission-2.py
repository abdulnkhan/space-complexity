class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
            - Declare result array - initialize to random number
            - l, r = 0, len of array
            - start while loop
                - if val(l) < val(r) - just return the left most value - break
                - Figure out if we're on left side or right side by comparing val at mid
                    - if val(m) >= rp -> search right side because obviously it cant
                    - else if val(m) >= lp search left side 
                    - think about if mid point is more than rp then the anwer can only be 
                      on the right side because its rotated

        """
        res = nums[0]
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            if nums[lp] < nums[rp]:
                res = min(res, nums[lp])
                break
            mp = (rp + lp) // 2
            res = min(res, nums[mp])

            if nums[mp] >= nums[lp]:
                lp = mp + 1
            else:
                rp = mp - 1

        return res