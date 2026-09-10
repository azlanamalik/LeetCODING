"""
This is a O(n^2)
best approach is an O(n)
check that methodology out

2 pointer reference

"""




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = 0
        i = 0  #left pointer
        temp = 0
        for x in range(0,len(prices)):
            for i in range(x, len(prices)):
                temp = prices[i] - prices[x] 
                if (max_val < temp) and temp > 0:
                    max_val = temp
            temp = 0
        
        return max_val


#with help

class Solution_second_try:
    def maxProfit(self, prices: List[int]) -> int:
            minimum_price = float("inf")
            max_profit = 0

            for price in prices:
                minimum_price = min(minimum_price, price)
                profit = price - minimum_price
                max_profit = max(max_profit, profit)

            return max_profit