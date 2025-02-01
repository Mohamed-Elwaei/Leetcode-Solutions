from collections import Counter
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        perm=Counter(s1)

        n=len(s1)

        for i in range(len(s2)-n+1):
            tmp=s2[i:i+n]
        
            tmpPerm=Counter(tmp)

            if tmpPerm==perm:
                return True
        return False