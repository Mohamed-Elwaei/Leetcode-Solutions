"""
energy = [5,2,-10,-5,1], k = 3


gains = [5,2,-10,0,3]


energy = [-2,-3,-1], k = 2
gains =  [-2,-3,-1]

let the last k indices of gains be the maximum value possible ending at the index
"""

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        
        n = len(energy)
        for i in range(k,n):
            energy[i] = max(energy[i],energy[i-k] + energy[i])


        ans = energy[-1]
        for i in range(n-1,n-1-k,-1):
            ans = max(ans,energy[i])
        return ans