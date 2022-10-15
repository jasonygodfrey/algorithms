class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
            
        return one
#time complexity: O(n)
#space complexity: O(1)

""" Here is the explanation for the code above:
1. This is a simple fibonacci sequence. The number of ways to climb to a step is the sum of ways to climb to the previous two steps. 
2. Therefore, we are going to create two variables to store the number of ways to climb to the previous two steps. In this case, it is 1.
3. Then, we are going to loop for n - 1 times. In each loop, we are going to store the number of ways to climb to the previous step in a temporary variable.
4. We are going to update the number of ways to climb to the previous two steps by adding the number of ways to climb to the previous step and the number of ways to climb to the step before the previous step.
5. Finally, we are going to return the number of ways to climb to the top step. """