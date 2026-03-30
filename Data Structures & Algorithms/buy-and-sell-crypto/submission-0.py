class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        n = len(prices)
        profit = 0

        for i in range(n):
            for j in range(i+1, n):
                temp = prices[j] - prices[i]
                if temp > profit:
                    profit = temp
        return profit
