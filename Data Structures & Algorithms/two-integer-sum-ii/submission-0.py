class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        a=[]
        while left<right:
            if numbers[left]+numbers[right]==target:
                a.append(left + 1)
                a.append(right + 1)
                break
            elif numbers[left]+numbers[right]>target:
                right-=1
            else:
                left+=1
        return a
        