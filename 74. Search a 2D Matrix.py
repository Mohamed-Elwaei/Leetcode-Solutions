class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0,len(matrix)-1
        def binSearch(nums,target):
            l,r = 0,len(nums)-1

            while l<=r:
                mid = (l+r)//2

                if nums[mid] == target:
                    return True
                if nums[mid]>target:
                    r = mid-1
                else:
                    l = mid+1
            return False

        while l<=r:
            mid = (l+r)//2

            if matrix[mid][0] <= target<=matrix[mid][-1]:
                return binSearch(matrix[mid],target)
            if matrix[mid][0] > target:
                r = mid-1
            else:
                l = mid+1
        
        return False