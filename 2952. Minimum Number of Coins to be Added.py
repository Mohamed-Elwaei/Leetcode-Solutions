"""
Use a set.

Make sure the length of the set is equal to target
"""


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        coins.sort()
        
        
        
        
        M = 0
        l = 0
        count = 0
        #At each iteration we can form [1,M] integers as a subsequence
        while M < target:
            
            if l >= len(coins) or coins[l] - 1 > M: # We need to add a coin M+1
                count += 1
                M += M+1
            else:
                M += coins[l]
                l+=1
        return count
                
            