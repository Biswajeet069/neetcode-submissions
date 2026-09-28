class Solution:
    def canJump(self, nums: List[int]) -> bool:

        l = len(nums) - 1
        flag = False
        reach = 0

        for i in range(len(nums)):

            if i > reach:
                break

            reach = max(reach, i + nums[i])

            if reach >= l:
                flag = True
                break

        return flag
