class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minval=float("inf")
        for i in range(0,len(prices)):
            minval=min(minval,prices[i])
            maxprofit=max(maxprofit,prices[i]-minval)
        return maxprofit
        