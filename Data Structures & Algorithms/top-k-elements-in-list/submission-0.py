class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a=[]
        d={}
        maxi=0
        for i in range(0,len(nums)):
            if nums[i] not in d:
                d[nums[i]]=1
            else:
                d[nums[i]]+=1
        arr=sorted(d.items(), key=lambda x: x[1], reverse=True)
        for i in range(0,k):
            a.append(arr[i][0])
        return a



        