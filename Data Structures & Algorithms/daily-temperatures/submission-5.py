class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=[]
        for i in range(0,len(temperatures)):
            count=0
            found = False
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    count+=1
                    a.append(count)
                    found = True
                    break
                else:
                    count+=1
            if not found:
                a.append(0)
        return a