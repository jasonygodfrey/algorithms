class Solution:
    def removeVowels(self, s: str) -> str:
        q = s.replace('a', '')
        r = q.replace('e', '')
        s = r.replace('i', '')
        t = s.replace('o', '')
        u = t.replace('u', '')
        
        return u