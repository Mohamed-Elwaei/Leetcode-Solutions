import heapq
class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        """
         nums = [1,2,2,1,2,3,1], queries = [[1,2],[3,3],[4,2]]
         total = 12
         
         nums = [N,N,2,N,2,3,1] queries = [[3,3],[4,2]]
         total = 8

         nums = [N,N,N,N,N,3,N] queries = [[4,2]]
         total = 3
         
         nums = [N,N,N,N,N,N,N] queries = [[4,2]]
         total = 0
            
        """
        
        
        N = len(nums)
        unmarked = {i for i in range(N)}
        
        heap =  []
        answer = []
        total = 0
        for i,n in enumerate(nums):
            heapq.heappush(heap, (n,i))
            total += n
        print(heap)
        for index, k in queries:
            if index in unmarked:
                unmarked.remove(index)
                total -= nums[index]
            
            while heap and k:
                number, index = heapq.heappop(heap)
                if index not in unmarked:
                    continue
                total -= number
                unmarked.remove(index)
                k -= 1
            answer.append(total)
        return answer
        