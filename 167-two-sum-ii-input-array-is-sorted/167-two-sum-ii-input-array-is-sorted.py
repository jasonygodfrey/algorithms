class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        
        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []
        """ Here is the explanation for the code above:
1. Initialize two pointers, left and right.
2. While left pointer is smaller than right pointer:
    a. Find the sum of the two numbers pointed by the two pointers.
    b. If the sum is greater than the target, move the right pointer to the left.
    c. If the sum is smaller than the target, move the left pointer to the right.
    d. If the sum is equal to the target, return the result.
3. If the two pointers meet each other, return the result. """