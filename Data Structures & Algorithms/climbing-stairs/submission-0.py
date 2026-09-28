class Solution:

    def climbStairs(self, n: int) -> int:

        a = [-1] * (n + 1)

        def st(stare, a):

            if stare == 1 or stare == 0:
                return 1

            if a[stare] != -1:
                return a[stare]

            a[stare] = st(stare-1, a) + st(stare-2, a)

            return a[stare]

        return st(n, a)