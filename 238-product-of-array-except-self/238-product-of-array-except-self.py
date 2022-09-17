class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0]*n
        answer[0] = 1
        for i in range(1, n):
            answer[i] = nums[i-1] * answer[i-1]
        R = 1
        for i in reversed(range(n)):
            answer[i] = answer[i] * R
            R *= nums[i]
        return answer
""" Here is the explanation for the code above:
1. First we create the variables we need, namely max_profit to store the maximum profit we can get, and min_price to store the minimum price we have seen so far.
2. Then we iterate through the prices array, at each index i.
3. If we have seen a price lower than the current minimum price, we update the minimum price.
4. Otherwise, we update the maximum profit we can get, by comparing the current maximum profit and the price at index i minus the current minimum price.
5. Finally, we return the maximum profit we can get. """