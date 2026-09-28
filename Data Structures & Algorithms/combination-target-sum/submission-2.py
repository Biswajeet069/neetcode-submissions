class Solution:

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result = []
        subset = []

        def solve(index, subset):

            if sum(subset) == target:
                result.append(subset.copy())
                return

            if sum(subset) > target:
                return

            if index >= len(nums):
                return

            subset.append(nums[index])
            solve(index, subset)

            subset.pop()
            solve(index + 1, subset)

        solve(0, subset)
        return result
            
            
        
        