class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
      

        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            temp = max_product
            max_product = max(nums[i], nums[i] * max_product, nums[i] * min_product)
            min_product = min(nums[i], nums[i] * temp, nums[i] * min_product)

            result = max(result, max_product)

        return result
            

        