class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(' ')
        s=s[::-1]
        ret=''
        print(s)
        for word in s:
            if word:
                ret+=word
                ret+=' '
        return ret[:-1]
           