class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()

        a = []

        for i in range(0, len(nums) - 3):

            for j in range(i + 1, len(nums) - 2):

                left = j + 1
                right = len(nums) - 1

                while right > left:

                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        a.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        left += 1
                        right -= 1

                    elif total > target:
                        right -= 1

                    else:
                        left += 1

        a = list(set(tuple(x) for x in a))
        a = [list(x) for x in a]

        return a
                    
        