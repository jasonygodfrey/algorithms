class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxwealthsofar = 0
        for account in accounts:
            ccw = sum(account)
            maxwealthsofar = max(maxwealthsofar, ccw)
        return maxwealthsofar