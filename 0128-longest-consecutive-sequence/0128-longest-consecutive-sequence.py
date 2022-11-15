class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        
        for n in nums:
            #check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest

""" Here is the explanation for the code above:
1. We create a set out of the given list of numbers.
2. We iterate through the list of numbers and check if the number is the start of a sequence. To do this, we check if the number minus 1 is not in the set.
3. If the number is the start of a sequence, we iterate through the set of numbers and check if the current number plus the length of the sequence is in the set.
4. We continue this process until we find a number that is not in the set.
5. We return the maximum length of the sequences that we found. """