class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        p=0
        q=0
        while p<len(t):
            if q>=len(s):
                return 1
            if t[p]==s[q]:
                q+=1
            p+=1 
        if q>=len(s):
            return 1
        return 0