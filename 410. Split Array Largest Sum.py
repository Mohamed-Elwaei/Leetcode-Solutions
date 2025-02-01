import heapq
def splitArray( nums: list[int], k: int) -> int:
        
        
        heap = [(-sum(nums),len(nums),nums)]
        ans = 0

        while heap and k>1:
            total,_,arr = heapq.heappop(heap)
            total*=-1
            if len(arr) == 1:
                ans  = max(ans,total)
                continue
            

            first,second = 0,total
            bpoint = (0,float('inf'))
            for i,num in enumerate(arr):
                bpoint = (i,max(first,second)) if max(first,second) < bpoint[1] else bpoint
                first+=num
                second-=num
            first,second = arr[:bpoint[0]],arr[bpoint[0]:]
            heapq.heappush(heap,(-sum(first),len(first),first))
            heapq.heappush(heap,(-sum(second),len(second),second))
            k-=1
        return max(ans,-heapq.heappop(heap)[0])


nums = [2,3,1,1,1,1,1]

k = 5
print(splitArray(nums,k))