class Solution:
    def reverseBits(self, n: int) -> int:

        result = []

        for i in range(32):
            bit = n & 1
            result.append(bit)
            n >>= 1

        s = ''.join(map(str, result))

        return int(s, 2)
        