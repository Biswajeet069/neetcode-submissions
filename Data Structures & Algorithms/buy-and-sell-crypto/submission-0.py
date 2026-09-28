class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi=0
        for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                a=prices[j]-prices[i]
                maxi=max(maxi,a)
        return maxi
        