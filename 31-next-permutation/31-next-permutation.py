class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pivot = None
        for i in range(len(nums)-1, 0, -1):
            if nums[i] > nums[i-1]:
                pivot = i-1
                break
        if pivot is None:
            nums.sort()
        else:
            for i in range(len(nums)-1, pivot, -1):
                if nums[i] > nums[pivot]:
                    nums[i], nums[pivot] = nums[pivot], nums[i]
                    break
            nums[pivot+1:] = nums[pivot+1:][::-1]
        



""" Here is the explanation for the code above:
1. We find the first element, which is smaller than its next element from the end of the array.
2. If we can't find such an element, we know that the array is already in descending order. In this case, we just reverse the array.
3. If we can find such an element, we know that the array is not in descending order. In this case, we find the next larger element from the end of the array and swap it with the first element we found.
4. Finally, we reverse the right part of the array, which is the part after the first element we found. """