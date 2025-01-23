class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = -1

        l, r = 0, 0

        for i, c in enumerate(prices):
            if prices[l] < prices[r]:
                if (prices[i] - prices[l]) > maxProfit:
                    maxProfit = prices[i] - prices[l] 
            else:
                l = r
            r = r + 1

        if maxProfit <= -1:
            return 0
        else:
            return maxProfit
        