class Solution:
    def countBits(self, n: int) -> List[int]:

        result = []

        for i in range(0, n + 1):

            count = 0
            x = i

            while x:
                if x & 1 == 1:
                    count += 1

                x >>= 1

            result.append(count)

        return result
             

        