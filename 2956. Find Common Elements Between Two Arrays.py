
class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr1,arr2 = nums1,nums2
        nums1,nums2 = set(nums1),set(nums2)
        
        first = 0
        for n in arr1:
            first += n in nums2
        second = 0
        for n in arr2:
            second += n in nums1
        
        return [first,second]