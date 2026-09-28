class Solution:
    def validPalindrome(self, s: str) -> bool:

        flag = False
        a = list(s)

        l = 0
        r = len(a) - 1

        while r > l:

            if a[l] != a[r]:
                b = a[l + 1:r+1 ]
                c = a[l:r]

                if b == b[::-1] or c == c[::-1]:
                    flag = True

                return flag

            l += 1
            r -= 1

        return True


        
        