class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp, rp = 0, len(nums) - 1

        while lp <= rp:
            m = int((lp + rp) / 2)

            if nums[m] > target:
                rp = m - 1
            elif nums[m] < target:
                lp = m + 1
            else:
                return m

        return -1     
    
# brute force

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        individualProfit = 0
        for i, price in enumerate(prices):
            for j in range(i+ 1, len(prices)):
                if individualProfit < (prices[j] - price):
                    individualProfit = prices[j] - price
            if maxProfit < individualProfit:
                maxProfit = individualProfit
        
        if(maxProfit <= -1):
            return 0
        else:
            return maxProfit
        