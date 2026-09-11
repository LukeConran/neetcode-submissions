class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0
        min_value = 101
        for i in range(len(prices)):
            max_price = max(prices[i]-min_value, max_price)
            min_value = min(prices[i], min_value)

        return max_price