class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        return max_sum
    """ Here is the explanation for the code above:
1. Create a variable called max_sum and assign it to the first element of the array.
2. Create a variable called current_sum and assign it to the first element of the array.
3. Loop through the array from the second element to the last element.
4. In each iteration, calculate the maximum between the current element and the sum of the current element and the current_sum.
5. Update the current_sum with the maximum value.
6. Calculate the maximum between the max_sum and the current_sum.
7. Return the max_sum. """