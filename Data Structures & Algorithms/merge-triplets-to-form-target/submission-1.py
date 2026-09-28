class Solution:

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        flag = False
        a = [0, 0, 0]

        for i in range(len(triplets)):
            if triplets[i][0] <= target[0] and triplets[i][1] <= target[1] and triplets[i][2] <= target[2]:
                for j in range(len(triplets[i])):
                    a[j] = max(a[j], triplets[i][j])

        if a == target:
            flag = True

        return flag

        