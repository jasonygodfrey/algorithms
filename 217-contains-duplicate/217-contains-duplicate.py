class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hellomap = set()
        
        for i in nums:
            if i in hellomap:
                return True
            hellomap.add(i)
        return False