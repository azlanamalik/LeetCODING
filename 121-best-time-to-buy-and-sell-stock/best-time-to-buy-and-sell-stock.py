class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 1:
            return 0
        l = 0
        r = 1
        maxPrice = -1
        while (r < len(prices)):
            if (prices[l] > prices[r]):
                l = r
            maxPrice = max(maxPrice , prices[r] - prices[l])
            r += 1
        return maxPrice