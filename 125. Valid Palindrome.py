class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        news=''

        for l in s:
            if l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                news+=l.lower()
            elif l in '0123456789abcdefghijklmnopqrstuvwxyz':
                news+=l
        p,q=0,len(news)-1
        while p<q:
            print(news[p],news[q])
            if news[p]!=news[q]:
                return False

            p+=1
            q-=1
        return True