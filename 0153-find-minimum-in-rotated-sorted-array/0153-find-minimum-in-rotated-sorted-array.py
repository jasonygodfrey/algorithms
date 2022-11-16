class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l<= r:
            if nums[l] < nums[r]:
                res= min(res, nums[l])
                break
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
        #time complexity: O(logn)
        # space complexity: O(1)
        """ The code above does the following:
1. Find the minimum element in the array using binary search.
2. If the array is already sorted, the minimum element will be at the start of the array, so we can just return the first element.
3. If the array is not sorted, we will have to check on which side of the array the minimum element lies.
4. If the minimum element lies on the left side, we will move our right pointer to the middle of the array.
5. If the minimum element lies on the right side, we will move our left pointer to the middle of the array.
6. We will keep on doing this until we find the minimum element in the array. """