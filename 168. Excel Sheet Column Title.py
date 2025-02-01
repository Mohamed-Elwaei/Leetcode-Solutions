from collections import deque
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ans = []
        tmp=columnNumber
        alphabet='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        while columnNumber:
            ans.append(alphabet[(columnNumber-1)%26])
            columnNumber = (columnNumber-1)//26

        
        
        return ''.join(ans[::-1])
