class Solution:

    def tribonacci(self, n: int) -> int:

        if n < 2:
            return n

        s = [-1] * (n + 1)

        s[0] = 0
        s[1] = 1
        s[2] = 1

        for i in range(3, len(s)):
            s[i] = s[i-1] + s[i-2] + s[i-3]

        return s[n]
        