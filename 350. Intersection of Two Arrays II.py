from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1)>len(nums2):return self.intersect(nums2,nums1)
        count=Counter(nums2)
        intersections=[]
        for i in nums1:
            if count[i]>0:
                count[i]-=1
                intersections.append(i)
        return intersections