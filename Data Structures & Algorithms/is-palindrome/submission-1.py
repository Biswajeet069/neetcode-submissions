class Solution:
    def isPalindrome(self, s: str) -> bool:
        result="".join(i for i in s if i.isalnum())
        a=result.lower()
        if a==a[::-1]:
            return True
        return False   