class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        powers = dict()

        def getPower(n):
            if n in powers:
                return powers[n]
            if n==1:
                powers[n] = 0
                return 0
            if  n%2 == 0:
                powers[n] = 1 + getPower(n/2)
            else:
                powers[n] = 1 + getPower((n*3) + 1)
            return powers[n]
        
        nums = [i for i in range(lo,hi+1)]

        nums.sort(key = lambda x: (getPower(x),x))
        

        return nums[k-1]
        