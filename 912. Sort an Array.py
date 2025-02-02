def merge_sort(arr):
    n = len(arr)
    if len(arr) == 1:
        return arr
    
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left,right)


def merge(A,B):
    i = j = 0
    C = []
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[j])
            j += 1
    
    while i < len(A):
        C.append(A[i])
        i+=1
    
    while j < len(B):
        C.append(B[j])
        j += 1
    return C


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return merge_sort(nums)
        