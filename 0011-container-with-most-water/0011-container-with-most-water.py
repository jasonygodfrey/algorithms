class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        
        l, r = 0, len(height) - 1
        while l < r:
            area = (r-l) * min(height[l], height[r])
            res= max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
                #time complexity: O(n)
                #space complexity: O(1)
"""Here is the explanation for the code above:
1. We use two pointers, one at the start (l) and one at the end (r) of the array.
2. We calculate the area between the two pointers, which is the area of the rectangle bounded by the two lines (height[l] and height[r]) and the distance between them (r-l).
3. We then update the result. This update is necessary because we want the max area possible, so we update if the current area is greater than the previous one.
4. We then need to move the pointers. Which pointer do we move? We move the pointer with the smaller height, because if we move the pointer with the larger height, we will still get a smaller area, because the distance between the two pointers decreases. """