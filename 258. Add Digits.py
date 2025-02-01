class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>=10:
            digits=[int(i) for i in str(num)]
            num=sum(digits)
        return num    