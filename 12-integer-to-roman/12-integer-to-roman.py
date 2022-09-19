class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        roman_num = ''
        while num > 0:
            for i in sorted(roman.keys(), reverse=True):
                if num >= i:
                    roman_num += roman[i]
                    num -= i
                    break
        return roman_num