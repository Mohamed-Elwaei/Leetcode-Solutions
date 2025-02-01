from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        dicts,dictt=defaultdict(int),defaultdict(int)

        if len(s)!=len(t):
            return False
        
        for i in range(len(s)):
            dicts[s[i]]+=1
            dictt[t[i]]+=1
        alphabet='abcdefghijklmnopqrstuvwxyz'

        for letter in alphabet:
            if dictt[letter]!=dicts[letter]: return False
        return True

        