class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l,r = -1,num+1

        while r-l>1:
            mid = (r + l) // 2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                r=mid
            else:
                l=mid
        return False