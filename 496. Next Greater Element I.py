class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        Map = dict()

        for i,n in enumerate(nums2):
            Map[n] = i
        Map2 = dict()
        for i,n in enumerate(nums1):
            Map2[i] = Map[n]
        


        st = []
        tmp = nums2[:]

        for i in range(len(nums2)-1,-1,-1):

            while st and st[-1] < nums2[i]:
                st.pop()
            tmp[i] = nums2[i] if not st else max(st[-1],nums2[i])
            st.append(nums2[i])
        nums2 = tmp
        ans = nums1[:]
        for i in range(len(nums1)):
            ans[i] = -1 if nums1[i] == nums2[Map2[i]] else nums2[Map2[i]]
        return ans
