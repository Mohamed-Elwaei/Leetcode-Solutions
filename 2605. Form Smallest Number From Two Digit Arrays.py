class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        
        S1 = set(nums1)
        S2 = set(nums2)
        
        ans = 20
        
        for n in S1:
            if n in S2:
                ans = min(n,ans)
        
        if ans != 20:
            return ans
        
        a = min(S1)
        b = min(S2)
        if a > b: a,b = b, a
        
        return 10*a + b