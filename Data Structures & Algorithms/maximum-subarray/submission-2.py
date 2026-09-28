class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=float("-inf")
        ans=float("-inf")
        for i in range(0,len(nums)):
            s=max(nums[i],s+nums[i])
            ans=max(ans,s)

        return ans


                

        