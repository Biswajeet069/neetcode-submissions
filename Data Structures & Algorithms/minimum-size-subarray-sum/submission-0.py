class Solution:

    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        a = list()
        left = 0
        mini = float("inf")

        for right in range(0, len(nums)):

            a.append(nums[right])

            while sum(a) >= target:
                mini = min(mini, right - left + 1)
                a.pop(0)
                left += 1

        if mini == float("inf"):
            return 0

        return mini


        