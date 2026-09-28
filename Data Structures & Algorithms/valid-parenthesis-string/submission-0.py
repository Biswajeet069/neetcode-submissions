class Solution:
    def checkValidString(self, s: str) -> bool:

        start = 0
        end = 0

        for i in range(len(s)):

            if s[i] == "(":
                start += 1
                end += 1

            elif s[i] == ")":
                start -= 1
                end -= 1

            else:
                start -= 1
                end += 1

            if end < 0:
                return False

            if start < 0:
                start = 0

        return start == 0
        
        

        
        