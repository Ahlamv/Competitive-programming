class Solution:
    def guessNumber(self, n: int) -> int:
        left,right=1,n
        while left<=right:
            mid=(left+right)//2
            ref=guess(mid)
            if ref==0:
               return mid
            elif ref<0:
               right=mid-1
            else:
               left=mid+1