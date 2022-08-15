class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        
        s = 0
        product = 1
        
        for i in n:
            s += int(i)
            product *= int(i)
            
        return product - s