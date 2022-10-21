class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 #base case
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
                    
        return dp[amount] if dp[amount] != amount + 1 else -1
        
        #o(amount * len(coins))
        #o(amount)
        """ The code above does the following:
1. Create an array of length amount + 1
2. Initialize the array to amount + 1
3. Set the first element to 0
4. For each amount a, we loop through each coin c
5. If the amount is greater than or equal to the coin
6. Set the amount equal to the minimum of the amount and 1 + the difference between the amount and the coin
7. Return the amount if it is less than or equal to the original amount, otherwise return -1 """