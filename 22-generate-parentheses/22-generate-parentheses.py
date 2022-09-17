#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

"""#Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

"""


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s = '', left = 0, right = 0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s+'(', left+1, right)
            if right < left:
                backtrack(s+')', left, right+1)
        backtrack()
        return res
    
""" The code above does the following, explained in English:
1. We start with an empty string, and 0 pairs of parentheses.
2. As long as the string has less than 2n characters, we can add another '(' or ')' character. If we add a '(' we'll have n+1 left parentheses, and n right parentheses. If we add a ')' we'll have n left parentheses and n+1 right parentheses.
3. When we have 2n parentheses, we know it's a valid sequence. """