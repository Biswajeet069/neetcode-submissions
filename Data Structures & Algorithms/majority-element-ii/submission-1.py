class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        d = dict()
        ans = []

        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1

        for num in d:
            if d[num] > len(nums) / 3:
                ans.append(num)

        return ans 
        