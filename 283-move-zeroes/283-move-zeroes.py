class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        return nums