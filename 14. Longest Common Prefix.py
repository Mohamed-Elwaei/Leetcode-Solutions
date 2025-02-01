class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)<1:return ''
        strs=sorted(strs)
        ret=''
        for i in range(min(len(strs[0]),len(strs[-1]))):
            if strs[0][i]!=strs[-1][i]:
                return ret
            ret+=strs[0][i]    
        return ret    