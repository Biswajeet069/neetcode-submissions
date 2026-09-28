class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        num = list(set(nums))
        num.sort()
        a = 1
        count = 1
        for i in range(len(num) - 1):
            if num[i] + 1 == num[i + 1]:
                count += 1
            else:
                count = 1
            a = max(a, count)
        return a

        