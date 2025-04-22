class Solution:
    def isPalindrome(self, x: int) -> bool:
        pal=str(x)
        s=pal[::-1]
        return pal==s