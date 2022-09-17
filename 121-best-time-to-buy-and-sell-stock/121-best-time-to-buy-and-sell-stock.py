class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_price)
        return max_profit
    
    """ Here is the explanation for the code above:
1. We initialize the maximum profit to be 0, and the minimum price to be the first element in the prices array.
2. We iterate through the prices array starting from the second element.
3. If the current element is smaller than the minimum price, we update the minimum price to be the current element.
4. Otherwise, we update the maximum profit to be the maximum of the current maximum profit and the difference between the current element and the minimum price.
5. We return the maximum profit at the end of the function. """