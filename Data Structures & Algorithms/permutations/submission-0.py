class Solution:

    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []
        used = [False] * len(nums)

        def solve(subset):

            if len(subset) == len(nums):
                result.append(subset.copy())
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                used[i] = True
                subset.append(nums[i])

                solve(subset)

                subset.pop()
                used[i] = False

        solve(subset)

        return result

            


        