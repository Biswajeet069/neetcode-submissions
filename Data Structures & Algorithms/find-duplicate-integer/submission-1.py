class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s=set()
        for i in range(0,len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                return nums[i]
        