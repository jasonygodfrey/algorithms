class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
                
        return True if not stack else False
    
    """ Here is the explanation for the code above:
1. Initialize an empty list named stack to store the open parenthesis.
2. Create a dictionary called closeToOpen to map the closing parenthesis to the corresponding opening parenthesis.
3. Iterate through the input string, s.
4. If the current character is a closing parenthesis, check if the top of the stack is the corresponding opening parenthesis. If it is, pop it. Otherwise, the input string is invalid.
5. If the current character is an opening parenthesis, push it onto the stack.
6. If the stack is empty, the input string is valid. Otherwise, the input string is invalid. """