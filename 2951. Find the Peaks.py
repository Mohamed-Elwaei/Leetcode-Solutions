class Solution:
    def findPeaks(self, A: List[int]) -> List[int]:
        peaks = []
        
        n = len(A)
        
        for i in range(1,n-1):
            if A[i] > A[i+1] and A[i] > A[i-1]:
                peaks.append(i)
        return peaks