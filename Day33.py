class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(-2**31 <= x and x <= 2**31 - 1):
            return str(x)[::-1] == str(x)
            