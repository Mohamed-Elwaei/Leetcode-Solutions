from collections import defaultdict
class Solution:
                
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(nums,k):
            l=0
            subarrays = 0
            for r in range(len(nums)):
                k-=nums[r]%2
                while k<0:
                    k+=nums[l]%2
                    l+=1
                subarrays += r-l+1

            return subarrays
        return atMost(nums,k) - atMost(nums,k-1)