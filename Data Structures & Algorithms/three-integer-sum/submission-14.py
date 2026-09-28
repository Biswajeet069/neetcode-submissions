class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s=set()
        i=0
        for i in range(0,len(nums)-1):
            right=len(nums)-1
            left=i+1
            while left<right:
                if nums[i]+nums[left]+nums[right]==0:
                    s.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                if nums[i]+nums[left]+nums[right]>0:
                    right-=1
                if nums[i]+nums[left]+nums[right]<0:
                    left+=1
        return [list(s) for s in s]
      



            


        