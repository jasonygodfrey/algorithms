class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        #[rob1, rob2, n, n+1, ...] recurance reelationship
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    """ Here is the explanation for the code above:
1. rob1: the max amount of money we can get from robbing the first i-1 houses
2. rob2: the max amount of money we can get from robbing the first i houses
3. temp: the max amount of money we can get from robbing the first i+1 houses
4. rob1 = rob2: we shift the rob1 by one house
5. rob2 = temp: we shift the rob2 by one house
6. temp = max(n + rob1, rob2): we update the temp value """