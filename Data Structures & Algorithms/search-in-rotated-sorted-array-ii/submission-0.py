class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        flag=False
        for i in range(0,len(nums)):
            if nums[i]==target:
                flag=True
                break
        return flag
        