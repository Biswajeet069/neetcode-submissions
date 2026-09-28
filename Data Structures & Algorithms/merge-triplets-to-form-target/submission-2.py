class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        a = [0, 0, 0]

        for x in triplets:

            if x[0] <= target[0] and x[1] <= target[1] and x[2] <= target[2]:

                a[0] = max(a[0], x[0])
                a[1] = max(a[1], x[1])
                a[2] = max(a[2], x[2])

        return a == target
        