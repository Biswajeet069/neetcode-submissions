class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        result = []
        subset = []
        a = []

        nums.sort()

        def solve(index, subset):

            if index >= len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[index])
            solve(index + 1, subset)

            subset.pop()
            solve(index + 1, subset)

        solve(0, subset)

        for i in range(0, len(result)):
            if result[i] not in a:
                a.append(result[i])

        return a
            
            
        