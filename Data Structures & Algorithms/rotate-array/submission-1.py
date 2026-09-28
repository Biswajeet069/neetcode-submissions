class Solution:

    def rotate(self, nums: List[int], k: int) -> None:

        k = k % len(nums)

        for i in range(0, k):
            nums[:] = [nums[-1]] + nums[0:-1]