class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        nums1 = [2,7,11,15], nums2 = [1,10,4,11]
        nums1 = [2,7,11,15], nums2 = [1,4,10,11]
                             indices = [0,2,1,3]
        nums1 optimal permutation = [2,11,7,15]

        nums1 = [8,12,24,32], nums2 = [13,25,32,11]
                              nums2 = [11,13,25,32]
                              indices = [3,0,1,2]
        ret = [24, 32, 8 , 12 ]
        """
        n = len(nums1)
        nums1.sort()
        queue = deque(sorted([(nums2[i],i) for i in range(n)]))
        
        optimal = [None] * n
        for num in nums1:
            if num > queue[0][0]:
                optimal[queue.popleft()[1]] = num
            else:
                optimal[queue.pop()[1]] = num
        return optimal

        