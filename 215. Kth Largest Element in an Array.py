from random import randint
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.randomized_select(nums,0,len(nums)-1,k)
    
    def randomized_select(self,A,p,r,i):
        pivot=self.randomized_partition(A,p,r)
        k=pivot-p+1
        if k==i:
            return A[pivot]
        elif k>i:
            return self.randomized_select(A,p,pivot-1,i)
        elif k<i:
            return self.randomized_select(A,pivot+1,r,i-k)

    def randomized_partition(self,A,p,r):
        pivot=randint(p,r)
        A[pivot],A[r]=A[r],A[pivot]
        return self.partition(A,p,r)
    def partition(self,A,p,r):
        pivot=A[r]
        i=p-1
        for j in range(p,r):
            if A[j]>=pivot:
                i+=1
                A[i],A[j]=A[j],A[i]
        A[i+1],A[r]=A[r],A[i+1]
        return i+1