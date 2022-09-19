class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        i = 0
        result = 0
        while i < len(s):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                result += roman[s[i + 1]] - roman[s[i]]
                i += 2
            else:
                result += roman[s[i]]
                i += 1
        return result
    """ Here is the explanation for the code above:
1. We can see that the the roman number is composed by some basic symbols, such as I, V, X, L, C, D, M. We can use a dictionary to store the value of each symbol.
2. We can see that the value of the roman number is composed by some basic symbols, such as I, V, X, L, C, D, M. We can use a dictionary to store the value of each symbol.
3. We use the while loop to go through the string s. We check if the current symbol is less than the next symbol. If so, we add the value of the next symbol minus the current symbol to the result. We also add 2 to the index of the string. If not, we add the value of the current symbol to the result. We also add 1 to the index of the string.
4. Finally, we return the result. """