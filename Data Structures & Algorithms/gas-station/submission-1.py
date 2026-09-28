class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total = 0
        b = 0
        x = 0
        excess = []

        for i in range(0, len(gas)):
            excess.append(gas[i] - cost[i])

        for x in range(0, len(gas)):
            total += gas[x] - cost[x]

            if total < 0:
                b = x + 1
                total = 0

        total = 0

        for x in range(0, len(gas)):
            total += gas[x] - cost[x]

        if total < 0:
            flag = -1
        else:
            flag = b

        return flag



        