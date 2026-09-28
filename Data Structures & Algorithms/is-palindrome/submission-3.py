class Solution:
    def isPalindrome(self, s: str) -> bool:

        flag = False
        l = s.lower()
        a = []

        for i in l:
            if i.isalnum():
                a.append(i)

        b = "".join(a)

        if b == b[::-1]:
            flag = True

        return flag 

        
        
