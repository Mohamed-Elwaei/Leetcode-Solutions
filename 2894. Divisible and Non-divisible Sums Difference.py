
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        ans = n*(n+1) // 2 #Sum of all numbers from 1 to n.
        
        
        
        for i in range(m,n+1,m):
            ans -= 2*i
        return ans