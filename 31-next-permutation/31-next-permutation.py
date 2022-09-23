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
1. We start from the end of the list and check if the current element is greater than its predecessor. If it is, we have found our pivot which is the element just before the current element. Otherwise, we continue to the next element.
2. If we have found our pivot, we start from the end of the list again and check if the current element is greater than our pivot. If it is, we have found our swap element which is the element just before the current element. Otherwise, we continue to the next element.
3. We swap our pivot with our swap element and reverse the part of the list after our pivot.
4. If we have not found our pivot, we reverse the entire list. """