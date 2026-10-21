
class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        while low < high:
            mid = (low + high) // 2
            d = 1
            total = 0

            for w in weights:
                if total + w > mid:
                    d += 1
                    total = 0
                total += w

            if d <= days:
                high = mid
            else:
                low = mid + 1

        return low


        