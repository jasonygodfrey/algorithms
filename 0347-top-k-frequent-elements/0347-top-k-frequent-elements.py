class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

                    """ Here is the explanation for the code above:
1. We create a dictionary to count the frequency of each number.
2. Then we create a list of lists. Each list in the list contains the numbers with the same frequency.
3. We then loop through the list of lists from the end to the beginning. For each list, we append the numbers in the list to the result list. If the length of the result list is equal to k, we return the result list. """