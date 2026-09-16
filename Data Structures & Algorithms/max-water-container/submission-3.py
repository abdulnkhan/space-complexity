class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = 0
        lp = 0
        rp = len(heights)-1
        
        while lp < rp:
            temp_area = (rp - lp) * min(heights[lp], heights[rp])

            if heights[rp] < heights[lp]:
                rp -= 1
            elif heights[lp] < heights[rp]:
                lp += 1
            else: 
                lp += 1

            area = max(area, temp_area)

        return area