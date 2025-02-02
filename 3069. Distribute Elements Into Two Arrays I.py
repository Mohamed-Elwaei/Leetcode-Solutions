class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        
        A = [nums[0]]
        B = [nums[1]]
        
        
        for i in range(2, len(nums)):
            if A[-1] > B[-1]:
                A.append(nums[i])
            else:
                B.append(nums[i])
        return A + B