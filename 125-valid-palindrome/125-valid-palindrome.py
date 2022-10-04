class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    """ Here is the explanation for the code above:
1. We use two pointers, l and r, to scan the string from left and right, respectively.
2. We use while-loop to skip all non-alphanumeric characters on the left side.
3. We use while-loop to skip all non-alphanumeric characters on the right side.
4. We use if-statement to check whether the two characters are equal or not.
5. We use l += 1 and r -= 1 to move the two pointers to the next position.
6. We use while-loop to repeat the process until the two pointers meet each other.
7. We return True if the two pointers meet each other, and return False if not. """