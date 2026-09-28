class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
        for i in range(0,len(tokens)):
            if tokens[i] not in  "/-+*": 
                a.append(int(tokens[i]))
            elif tokens[i]=="+":
                b=a[-2]+a[-1]
                a.pop()
                a.pop()
                a.append(b)
            elif tokens[i]=="-":
                b=a[-2]-a[-1]
                a.pop()
                a.pop()
                a.append(b)
            elif tokens[i]=="/":
                b=int(a[-2]/a[-1])
                a.pop()
                a.pop()
                a.append(b)
            elif tokens[i]=="*":
                b=a[-1]*a[-2]
                a.pop()
                a.pop()
                a.append(b)
        return a[0]


            
        