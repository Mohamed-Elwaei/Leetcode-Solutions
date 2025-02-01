class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a % b)
        n = len(nums)
        k %= n
        GCD = gcd(n,k)

        for i in range(GCD):   
            curr = nums[i]
            for _ in range(n // GCD):

                next = nums[(i + k) % n]
                nums[(i + k) % n] = curr
                i = (i + k) % n
                curr = next
        return nums


        