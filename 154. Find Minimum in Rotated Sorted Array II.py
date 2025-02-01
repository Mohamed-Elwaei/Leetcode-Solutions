class Solution:
    def findMin(self, arr: List[int]) -> int:
        n = len(arr)
        l,r = 0, n - 1
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] > arr[r]:
                l = mid + 1
            elif arr[mid] < arr[l]:
                r = mid 
            else:
                r-=1
        return arr[l]