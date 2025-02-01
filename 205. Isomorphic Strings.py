class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hmap1=collections.defaultdict(lambda: '')
        hmap2=collections.defaultdict(lambda: '')
        if len(s)!=len(t):return False
        for i in range(len(s)):
            if hmap1[s[i]]!=t[i] and hmap1[s[i]]!='':
                return False
            if hmap2[t[i]]!=s[i] and hmap2[t[i]]!='':
                return False
            hmap1[s[i]]=t[i] 
            hmap2[t[i]]=s[i]
        return True  