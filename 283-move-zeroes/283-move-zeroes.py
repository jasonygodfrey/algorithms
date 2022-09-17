class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        return nums
    
""" The code above does the following, explained in English:
1. Iterate through the list of numbers.
2. If the number is zero, remove it from the list and append it to the end of the list.
3. Return the list. """