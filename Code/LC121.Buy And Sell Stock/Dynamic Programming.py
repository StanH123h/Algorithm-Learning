from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        min_price = prices[0]
        dp_max_profit = []
        for i in range(len(prices)):
            profit = prices[i] - min_price
            if not dp_max_profit:
                dp_max_profit.append(max(0, profit))
            else:
                dp_max_profit.append(max(dp_max_profit[i - 1], profit))
            min_price = min(min_price, prices[i])
        return dp_max_profit[-1]
