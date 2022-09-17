class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
            
""" Here is the explanation for the code above:
1. We create a for loop that will iterate over each element in the list.
2. Then we check if the element occurs only once in the list by using the count() method.
3. If the element occurs only once, we return it. """