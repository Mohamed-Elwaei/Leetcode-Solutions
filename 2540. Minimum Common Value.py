class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        a,b = 0,0
        while a < len(nums1) and b < len(nums2):
            if nums1[a] > nums2[b]:
                b += 1
            elif nums1[a] < nums2[b]:
                a += 1
            else:
                return nums1[a]
        return -1