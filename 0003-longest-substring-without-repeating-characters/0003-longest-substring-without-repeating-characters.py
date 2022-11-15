class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r- l + 1)
        return res
    """ Here is the explanation for the code above:
1. we make a set to store the characters in the substring
2. l is the left index of the substring, r is the right index of the substring
3. we move the right index to the right and check if the new character is in the set. If it is, we remove the leftmost character from the set, and move the left index to the right. We keep doing this until the new character is not in the set.
4. We add the new character to the set, and update the max length of the substring
5. return the max length """