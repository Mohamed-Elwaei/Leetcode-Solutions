class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 1
        tmp=n^-1
        ans=0
        while tmp&-tmp <n:
            if tmp&-tmp >n:
                return ans
            ans+=tmp&-tmp

            tmp=tmp&(tmp-1)
        return ans