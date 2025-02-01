class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """3 cases to consider
        1. Array has no zeros
        2. Array has 1 zero
        3. Array has no zeroes"""
        # n = len(nums)
        zeroes = 0 #How many zeroes we have
        arrayProduct = 1
        for n in nums: #O(n)
            if n != 0:
                arrayProduct *= n
            elif n == 0:
                zeroes += 1
                if zeroes >= 2:
                    return [0] * len(nums)
        output = [None ] * len(nums)
        if zeroes == 1:
            for i in range(len(nums)): #O(n)
                if nums[i] != 0:
                    output[i] = 0
                else:
                    output[i] = arrayProduct
        elif zeroes == 0:
            for i in range(len(nums)): #O(n)
                output[i] = arrayProduct // nums[i]
        return output
        #Time complexity: O(2n) => O(n)
        #Memory complexity: O(1)