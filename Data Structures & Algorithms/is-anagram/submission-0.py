class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag=False
        a=sorted(s)
        b=sorted(t)
        if a==b:
            flag=True
        return flag
        