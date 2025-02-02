class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        #Brute force solution: O(n^2)

        #Prefix Sum?
        #nums   = [1,-3,2,3,-2]
        #prefix = [1,-2,0,3,-1]

        #nums = [2,-5,1,-4,3,-2]
        #prefix = [2,-3,-2,-6,-3,-5]

        #Dimensions: index
        
        # for i in range(N):
        #     what's the largest subarray that has nums[i]
        
        N = len(nums)

        Min, Max = 0, 0 

        answer = 0
        prefixSum = 0
        for i in range(N):
            prefixSum += nums[i]
            #Largest absolute sum of subarray that ends at index i
            if prefixSum > 0:
                answer = max(answer, abs(prefixSum - Min))
            elif prefixSum < 0:
                answer = max(answer, abs(prefixSum - Max))
            else: 
                answer = max(answer, Max, abs(Min))
            Min = min(Min,prefixSum)
            Max = max(Max,prefixSum)
        return answer