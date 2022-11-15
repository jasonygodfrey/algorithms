class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        
        maxf = 0 #optimization
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            
            maxf = max(maxf,  count[s[r]]) #optimization
            
            while (r - l + 1) - maxf >  k:
                count[s[l]] -= 1
                l += 1
                
            
            res = max(res, r - l + 1)
        return res
    
    """ Here is the explanation for the code above:
1. We use the sliding window approach. We use two pointers l and r to keep track of the sliding window.
2. We keep track of the frequency of each character in the sliding window using the dictionary count.
3. We keep track of the maximum frequency maxf in the sliding window. 
4. We use the following condition to check if the sliding window is valid or not:
    a. (r - l + 1) - maxf <= k
    b. (r - l + 1) is the size of the sliding window
    c. maxf is the maximum frequency of a character in the sliding window
    d. k is the given number
5. If the condition fails, we remove the character at the left pointer and increment the left pointer by 1.
6. We update the result whenever the condition passes.
7. We return the maximum value of the result res.
8. Time complexity: O(n)
9. Space complexity: O(1) """