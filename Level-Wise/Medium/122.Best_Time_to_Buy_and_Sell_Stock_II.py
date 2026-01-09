class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        total = 0
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            elif price > min_price:
                total += price - min_price
                min_price = price
        return total
