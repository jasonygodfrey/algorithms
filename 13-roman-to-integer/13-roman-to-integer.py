class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result -= roman[s[i]]
            else:
                result += roman[s[i]]
        return result

    """ Here is the explanation for the code above:
    1. First, we initialize a dictionary that maps each roman character to its corresponding integer value.
    2. We initialize the result variable with 0.
    3. We loop through the string and check if the current character is smaller than the next character. If it is, we subtract its value from the result. If it is not, we add its value to the result.
    4. After we finish looping through the string, we return the result. """