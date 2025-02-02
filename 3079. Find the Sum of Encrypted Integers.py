class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        
        def convert(x):
            biggest = 0
            digits = 0
            while x:
                biggest = max(biggest, x % 10)
                digits += 1
                x //= 10
            return (biggest,digits)
        
        for i,x in enumerate(nums):
            biggest, digits = convert(x)
            nums[i] = 0
            while digits:
                nums[i] *= 10
                nums[i] = nums[i] + biggest
                digits -= 1
        return sum(nums)
                