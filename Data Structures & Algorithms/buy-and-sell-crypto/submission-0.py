class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0
        rp = 1
        maxProfit = 0
        while rp < len(prices):
            if prices[lp] > prices[rp]:
                lp = rp
                rp = rp + 1
            else:
                profit = prices[rp] - prices[lp]
                maxProfit = max(maxProfit, profit)
                rp = rp + 1
        return maxProfit