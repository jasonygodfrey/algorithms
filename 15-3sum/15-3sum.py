class Solution:
    #idk copied
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSumII(nums, i, res)
        return res

    def twoSumII(self, nums: List[int], i: int, res: List[List[int]]):
        lo, hi = i + 1, len(nums) - 1
        while (lo < hi):
            sum = nums[i] + nums[lo] + nums[hi]
            if sum < 0:
                lo += 1
            elif sum > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                    """ Here is the explanation for the code above:
1. sort the array
2. use a for loop to loop through the array
3. if the number is greater than 0, break the loop
4. if the number is not the same as the number before it, call the function twoSumII
5. in the function twoSumII, use two pointers lo and hi to find two numbers that add up to the negative of the number at i
6. if the sum is less than 0, move the lo pointer to the right
7. if the sum is greater than 0, move the hi pointer to the left
8. if the sum is 0, add the three numbers to the result list and move the lo and hi pointers to the right and left
9. if the lo pointer is the same as the number before it, move the lo pointer to the right
10. if the hi pointer is the same as the number after it, move the hi pointer to the left """