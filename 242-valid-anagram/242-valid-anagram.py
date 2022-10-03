class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
    """ Here is the explanation for the code above:
1. If the length of two strings are different, they are not anagrams.
2. Store the frequency of each character in the two strings in two dictionaries.
3. Iterate through the dictionary of string s, and check if the frequency of each character in string s is equal to the frequency of the character in string t.
4. If the frequency is not equal, then the two strings are not anagrams. """
    """ Here is the explanation for the code above:
1. If the lengths of two strings are different, they are not anagrams. 
2. Create two dictionaries to store the characters in s and t. 
3. For each character in s, we add 1 to the value of the dictionary countS. 
4. For each character in t, we add 1 to the value of the dictionary countT. 
5. For each character in countS, we check whether it's in countT and the value of countS is equal to the value of countT. 
6. If all the characters in countS are in countT and the value of countS is equal to the value of countT, then the two strings are anagrams. 
7. Return True. 
8. If not, return False. """