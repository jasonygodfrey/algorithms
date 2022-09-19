class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50], ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]
        
        res = ""
        for sym, val in reversed(symList):
            if num // val:
                count = num // val
                res += sym * count
                num = num % val
        return res
    """1. We store the symbols and their values in a list of lists.
2. We iterate through the list from the end to the beginning, and for each symbol, we divide the given number by the value of the symbol. If the result is greater than zero, it means that the symbol is smaller than the given number. We add the symbol to the result string as many times as the quotient is, and update the number by taking the remainder of the division.
3. We return the result string. """