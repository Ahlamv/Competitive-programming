class Solution:
    def addDigits(self, num: int) -> int:
        number=str(num)
        n=len(number)
        if num==0:
            return 0
        else:
            return 1+(num-1)%9