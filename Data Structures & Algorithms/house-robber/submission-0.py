class Solution:

    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        s = [-1] * (n + 1)

        def dp(index):

            if index >= n:
                return 0

            if s[index] != -1:
                return s[index]

            s[index] = max(
                nums[index] + dp(index + 2),
                dp(index + 1)
            )

            return s[index]

        return dp(0)

            
        