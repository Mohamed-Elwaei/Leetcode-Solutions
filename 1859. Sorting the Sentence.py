
from collections import defaultdict
class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(' ')
        ans=''
        hmap=defaultdict(str)
        size=0
        for word in s:
            i=0
            size+=1
            while not word[i].isdigit():
                i+=1
            hmap[int(word[i:])]=word[:i]
        for i in range(size+1):
            ans+=hmap[i]
            ans+=' '
        ans=ans[1:]    
        ans=ans[:-1]    
        return ans    