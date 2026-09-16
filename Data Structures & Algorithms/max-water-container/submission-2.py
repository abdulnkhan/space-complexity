class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        rp = len(heights) - 1
        area = 0
        while lp < rp:
            temp_area = (rp - lp) * min(heights[rp], heights[lp])
            area = max(area, temp_area)
            if heights[lp] < heights[rp]:
                lp += 1
            elif heights[rp] < heights[lp]:
                rp -= 1
            else:
                lp += 1
        return area
