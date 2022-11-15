class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        dict_t = Counter(t)
        required = len(dict_t)
        l, r = 0, 0
        formed = 0
        window_counts = {}
        ans = float("inf"), None, None
        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r += 1
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]
    """ Here is the explanation for the code above:
1. First, we create a dictionary dict_t to save the frequency of every character in t.
2. Then, we set two pointers l and r to represent the current window.
3. We use the variable required to save the number of unique characters in t, which will be used to compare with the variable formed later.
4. We use the dictionary window_counts to save the frequency of every character in the current window. 
5. We use the variable formed to save the number of unique characters in the current window which equals to the corresponding characters in t.
6. We use the variable ans to save the final result, which is a tuple including the length of the substring, the left pointer, and the right pointer.
7. We use a while loop to iterate through the string s. In each iteration, we move the right pointer r to the right by 1. 
8. We use the variable character to represent the character at the position r, and then we add 1 to the value of window_counts[character].
9. If the character is in dict_t and the frequency of the character in the current window equals to the frequency of the character in t, we add 1 to the variable formed.
10. Then, we use a while loop to shrink the current window. In each iteration, we move the left pointer l to the right by 1. 
11. We use the variable character to represent the character at the position l, and then we subtract 1 from the value of window_counts[character].
12. If the character is in dict_t and the frequency of the character in the current window is less than the frequency of the character in t, we subtract 1 from the variable formed.
13. Then, we check if the length of the current window is less than the length of the previous minimum window. If so, we update the variable ans.
14. Finally, we return "" if the length of the minimum window is infinity. Otherwise, we return the substring using the left and right pointers saved in the variable ans. """
    """ The code above does the following:
1. Creates a dictionary to store the characters in t and their counts.
2. Sets the required count to the length of the dictionary.
3. Creates a dictionary to store the characters in the current window and their counts.
4. Sets the formed count to zero.
5. Sets the answer to infinity, None, None.
6. Loops through s and adds the characters to the window dictionary.
7. Checks to see if the character is in t and if its count is equal to the count in t.
8. If the character is in t and its count is equal to the count in t, it increments the formed count.
9. Checks to see if the formed count is equal to the required count.
10. If the formed count is equal to the required count, it checks to see if the current window size is less than the answer.
11. If the current window size is less than the answer, it sets the answer to the current window size, left pointer, and right pointer.
12. It then removes the character from the left pointer from the window dictionary and decrements the count.
13. It then checks to see if the character is in t and the count is less than the count in t.
14. If the character is in t and the count is less than the count in t, it decrements the formed count.
15. It then increments the left pointer.
16. It then increments the right pointer.
17. It then returns an empty string if the answer is infinity or the substring of s from the left pointer to the right pointer + 1. """