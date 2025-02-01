class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0: return '0'
        ans=''

        hexas=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']


        for _ in range(8):
            curr=num&(0b1111)
            if num==0:
                break
            ans+=hexas[curr]
            num>>=4
        return ans[::-1]