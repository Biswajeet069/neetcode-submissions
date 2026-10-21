
# The guess API is already defined.
# @param num, your guess
# @return -1 if num is higher than pick
#          1 if num is lower than pick
#          0 if num equals pick

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2

            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                high = mid - 1
            else:
                low = mid + 1


        
        