class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            tmp = curMax * n
            curMax = max(n * curMax, n * curMin, n)
            curMin = min(tmp, n * curMin, n)
            res = max(res, curMax, curMin, n)
        return res
    """ The code above does the following:
1. Initialize max_sum to the first element of the array
2. Initialize current_sum to the first element of the array
3. Loop through the array starting from the second element
4. At each step, we update current_sum to be the maximum of the current element or the current element plus the current_sum
5. We update max_sum to be the maximum of max_sum and current_sum
6. Return max_sum """