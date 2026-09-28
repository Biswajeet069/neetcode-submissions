class Solution:
    def isValid(self, s: str) -> bool:
        a = list(s)
        b = []
        x = True

        for i in range(len(a)):
            if a[i] == "(" or a[i] == "[" or a[i] == "{":
                b.append(a[i])

            elif a[i] == ")" or a[i] == "]" or a[i] == "}":

                if len(b) == 0:
                    x = False
                    break

                if b[-1] == "(" and a[i] != ")":
                    x = False
                    break
                elif b[-1] == "[" and a[i] != "]":
                    x = False
                    break
                elif b[-1] == "{" and a[i] != "}":
                    x = False
                    break

                b.pop()

        if len(b) != 0:
            x = False

        return x  