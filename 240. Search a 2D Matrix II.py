def binary_search(arr,target):
    L,R=0,len(arr)-1

    while L<=R:
        mid = L + (R-L)//2
        if target == arr[mid]:
            return True
        elif arr[mid] > target:
            R = mid-1
        else:
            L = mid+1
    return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if binary_search(row,target):
                return True
        return False
        