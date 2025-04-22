class Solution:
    def trailingZeroes(self, n: int) -> int:
        fact=1
        for i in range(1,n+1):
            fact*=i
        j=0
        while fact>0:
            if fact%10==0:
                j+=1
                fact//=10
            else:break
        return j

            
        