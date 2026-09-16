class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lp = 0
        rp = lp + 1
        max_profit = 0

        while lp < rp and rp < len(prices):
            if prices[rp] < prices[lp]:
                lp = rp
                rp += 1
            else:
                profit = prices[rp] - prices[lp]
                max_profit = max(profit, max_profit)
                rp += 1

        return max_profit