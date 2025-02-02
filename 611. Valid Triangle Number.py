class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        #In a triangle with sides a,b,c a + b > c where c is the largest size
        def bs(firstSide,secondSide, l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if firstSide + secondSide <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l


        count = 0
        nums.sort()
        for a in range(len(nums)):
            for b in range(a + 1, len(nums)):
                largest_valid_side = bs(nums[a],nums[b], b + 1, len(nums) - 1)

                count += max(largest_valid_side - b - 1, 0)

        return count