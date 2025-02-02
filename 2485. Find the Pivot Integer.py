class Solution:
    def pivotInteger(self, n: int) -> int:
        l,r = 1, n
        while l <= r:
            mid = l + (r - l) // 2
            leftSum = (mid * (mid + 1)) // 2
            rightSum = ((n * (n + 1)) // 2) - leftSum + mid
            if leftSum > rightSum:
                r = mid - 1
            elif leftSum < rightSum:
                l = mid + 1
            else:
                return mid
        return -1