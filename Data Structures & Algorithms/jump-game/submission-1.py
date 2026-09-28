class Solution:
    def canJump(self, nums: List[int]) -> bool:

        flag = False
        l = len(nums)
        i = 0
        farthest = 0

        while i <= farthest:

            farthest = max(farthest, i + nums[i])

            if farthest >= l - 1:
                flag = True
                break

            i += 1

        return flag


        