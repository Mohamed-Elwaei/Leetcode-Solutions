class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        #Loop over the array
        #Iteration i:
        # include all the elements between [i,nums[i]]

        
        chunks = 0
        end = -1
        for i,n in enumerate(arr):
            if i > end:
                chunks += 1
            end = max(end, n)
        return chunks