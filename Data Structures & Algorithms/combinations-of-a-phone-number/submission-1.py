class Solution:

    def letterCombinations(self, digits: str) -> List[str]:

        subset = []
        result = []

        if digits == "":
            return []

        d = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def solve(index, subset):

            if index == len(digits):
                result.append("".join(subset))
                return

            for x in d[digits[index]]:

                subset.append(x)

                solve(index + 1, subset)

                subset.pop()

        solve(0, subset)

        return result
            
            
            
        