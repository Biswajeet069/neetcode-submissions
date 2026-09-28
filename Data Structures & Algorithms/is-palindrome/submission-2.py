class Solution:
    def isPalindrome(self, s: str) -> bool:
        result=[]
        l=s.lower()
        a=list(l)
        b="".join(a)
        flag=False
        for i in range(0,len(b)):
            if b[i].isalnum():
                result.append(b[i])
        if result==result[::-1]:
            flag=True
        return flag
        
