class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag=False
        a=set()
        for i in range(0,len(nums)):
            if nums[i] not in a:
                a.add(nums[i])
            else:
                flag=True
                break
        return flag

        


        