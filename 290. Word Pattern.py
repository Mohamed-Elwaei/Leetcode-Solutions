import collections
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        s=s.split(' ')
        hmap1=collections.defaultdict(lambda: '')
        hmap2=collections.defaultdict(lambda: '')
        if len(s)!=len(pattern):return False
        for i in range(len(pattern)):
            if hmap1[pattern[i]]!=s[i] and hmap1[pattern[i]]!='':
                return False
            if hmap2[s[i]]!=pattern[i] and hmap2[s[i]]!='':
                return False
            hmap1[pattern[i]]=s[i] 
            hmap2[s[i]]=pattern[i]
        return True    