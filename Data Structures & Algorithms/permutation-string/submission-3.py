class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        a=list(s1)
        b=list(s2)
        ds1={}
        ds2={}
        flag=False
        for i in range(len(a)):
            if a[i] not in ds1:
                ds1[a[i]]=1
            else:
                ds1[a[i]]+=1
        left = 0

        for right in range(len(s2)):
            if s2[right] not in ds2:
                ds2[s2[right]] = 1
            else:
                ds2[s2[right]] += 1
            if right-left+1>=len(a):
                if ds1==ds2:
                    flag=True
                ds2[s2[left]]-=1
                if ds2[s2[left]]==0:
                    del ds2[s2[left]]
                left+=1
        return flag

            
        
        
        
            