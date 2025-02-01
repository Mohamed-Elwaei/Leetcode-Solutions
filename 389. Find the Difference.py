from collections import Counter
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s_count=Counter(s)
        t_count=Counter(t)

        for i in range(ord('a'),ord('z')+1):
            if s_count[chr(i)]!=t_count[chr(i)]:return chr(i)
        return ''    