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