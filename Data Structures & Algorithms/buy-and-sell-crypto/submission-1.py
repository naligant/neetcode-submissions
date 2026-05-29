class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        end = 1
        max_ = 0
        while end != len(prices):
            if prices[start] >= prices[end]:
                start = end
            elif prices[start] < prices[end]:
                if prices[end] - prices[start] > max_:
                    max_ = prices[end] - prices[start]
            end += 1
        return max_

        
