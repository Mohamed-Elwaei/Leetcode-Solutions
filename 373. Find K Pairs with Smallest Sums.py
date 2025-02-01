import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #nums1 = [1,7,11], nums2 = [2,4,6], k = 3
        #initially: heap = [(3,1,2)]
        #after 1 iter: heap = [(5,1,4),(9,7,2)]
                #nums1[i] + nums2[j], current index of nums1, current index of nums2
        heap = [(nums1[i] + nums2[0],i,0) for i in range(min(k,len(nums1)))]
        heapq.heapify(heap)
        output = []

        for _ in range(k):
            sum, index1, index2 = heapq.heappop(heap)
            output.append((nums1[index1],nums2[index2]))

            if index2 < len(nums2) - 1:
                heapq.heappush(heap,(nums1[index1] + nums2[index2 + 1],index1,index2 + 1))
        

        return output