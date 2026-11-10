class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       
        l = 0
        r = 1
        bestCase = 0

        while l < len(prices) - 1:
            if prices[r] - prices[l] > bestCase:
                bestCase = prices[r] - prices[l]
            elif r == len(prices) - 1:
                l += 1
                r = l + 1
            else:
                r += 1
        return bestCase
        

