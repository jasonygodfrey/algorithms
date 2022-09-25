from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        SList = SortedList()
        for i in range(len(nums)):
            if i > k: SList.remove(nums[i-k-1])   
            pos1 = SortedList.bisect_left(SList, nums[i] - t)
            pos2 = SortedList.bisect_right(SList, nums[i] + t)
            
            if pos1 != pos2 and pos1 != len(SList): return True
            
            SList.add(nums[i])
        
        return False

""" Here is the explanation for the code above:
1. First, we need to import the sorted container package
2. Then, we have a function containsNearbyAlmostDuplicate which takes in three parameters: nums, k and t
3. We create a sorted list SList
4. We use a for loop to iterate through the nums list
5. We check if the length of nums is greater than k. If it is, we remove the element at index i-k-1
6. We create a variable pos1 to find the position of the number in SList that is just greater than or equal to nums[i] - t
7. We create a variable pos2 to find the position of the number in SList that is just greater than nums[i] + t
8. We check if pos1 is not equal to pos2 and pos1 is not equal to the length of SList. If it is, we return True
9. If not, we add the number nums[i] to SList
10. Finally, we return False """