class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp=num^-1

        ans=0

        while ans<num:
            if tmp&-tmp>num:
                return ans
            ans+=tmp&-tmp

            tmp=tmp&(tmp-1)
        return ans