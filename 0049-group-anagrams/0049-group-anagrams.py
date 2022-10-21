class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping charCount to list of Anagrams
        for s in strs:
            count = [0] * 26 
            for c in s:
                count[ord(c) - ord("a")] += 1
                
            res[tuple(count)].append(s)
            
        return res.values()
    """ Here is the explanation for the code above:
1. defaultdict(list) creates a dict with list as default value. 
2. count = [0] * 26 is a list of 26 zeros. 
3. count[ord(c) - ord("a")] += 1 means that the count of the letter c is increased by 1. 
4. res[tuple(count)].append(s) means that we map the count to the anagram. 
5. res.values() returns the values of the dict which is a list of lists. """