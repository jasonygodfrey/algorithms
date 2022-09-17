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
1. The answer array is used to store the product of all the numbers to the left of each index.
2. R is used to store the product of all the numbers to the right of each index.
3. We then iterate through the array in reverse order, and update answer[i] = answer[i] * R, where R would contain the product of all the numbers to the right of i.
4. We update R = R * nums[i] to contain the product of all the numbers to the right of the current index. """