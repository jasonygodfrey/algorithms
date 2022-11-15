"""There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity."""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            #left side is sorted
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            #right side is sorted
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
    """ Here is the explanation for the code above:
1. Find the middle element
2. If middle element is the target, return the index
3. If left side of the middle is sorted, and target is in the left side, then search left side, otherwise search the right side
4. If right side of the middle is sorted, and target is in the right side, then search right side, otherwise search the left side """
    """ The code above does the following, explained in English:
1. Set two pointers, one to the beginning of the list, one to the end.
2. While the left pointer is less than or equal to the right pointer:
    a. Find the middle index of the list.
    b. If the value at the middle index is equal to the target, we are done.
    c. If the value at the left index is less than or equal to the value at the middle index, we know the left side is sorted.
        i. Check if the target is greater than the value at the middle index, or less than the value at the left index.
            1. If either of these are true, the target cannot be in the left side of the list, so we set the left pointer to the middle index plus one.
            2. If both of these are false, the target is in the left side of the list, so we set the right pointer to the middle index minus one.
    d. If the value at the left index is greater than the value at the middle index, we know the right side is sorted.
        i. Check if the target is less than the value at the middle index, or greater than the value at the right index.
            1. If either of these are true, the target cannot be in the right side of the list, so we set the right pointer to the middle index minus one.
            2. If both of these are false, the target is in the right side of the list, so we set the left pointer to the middle index plus one.
3. If the left pointer is greater than the right pointer, we have searched the entire list and the target is not in it, so we return -1. """