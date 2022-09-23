class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        return max_area
""" Here is the explanation for the code above:
1. We use a stack to store the index of the bars.
2. If the current bar is higher than the last bar in the stack, we push its index to the stack.
3. If the current bar is lower than the last bar in the stack, we keep popping the stack until the current bar is higher than the last bar in the stack.
4. Each time we pop the stack, we calculate the max area with the popped bar as the smallest bar.
5. The stack may not be empty after the loop, so we need to calculate the areas with every bar as the smallest bar. """