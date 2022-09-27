class Solution:
    # calculate the sum of presums for certain strength at index i
    # we will use it in calculating the sum of all subarrays containing particular element
    # we stuff it with an extra value at the end to accomodate the lookups at -1 for left 
    # boundary which includes the beginning of the array
    def get_presums(self, strength):
        n  = len(strength)
        res = [0] * (n + 2)
        cur_sum = 0
        
        for i in range(n):
            cur_sum += strength[i]
            res[i+1] = (res[i] + cur_sum)
                    
        return res
            
    def totalStrength(self, strength: List[int]) -> int:
        if not strength:
            return 0
        
        n = len(strength)
        res = 0
        stack = []
        
        pre_sums = self.get_presums(strength)
                
        # use monotonic stack to find the min for a certain range of subarrays
        # and add an extra element at the end of the iterable to make sure we'll pop all elements
        # from the stack
        for i, num in enumerate(itertools.chain(strength, [-float('inf')])):
            while stack and num < strength[stack[-1]]:
                cur_min_idx = stack.pop()
                left  = stack[-1] if stack else -1
                
                # the TOTAL of all subarrays containing our minimum strength found above
                cur_sub_sum = (cur_min_idx - left) * (pre_sums[i] - pre_sums[cur_min_idx]) - (i - cur_min_idx ) * (pre_sums[cur_min_idx] - pre_sums[left])
                res +=  cur_sub_sum * strength[cur_min_idx]
                        
            stack.append(i)
                
        # i didn't use modular arithmetic along the way and only indicated its use here
        # cause in python int numbers don't have the limitation they may have in other languages
        return res % (10**9 + 7)