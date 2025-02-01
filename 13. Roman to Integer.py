class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        vals={'I':1,'V':5,'IV':4,'X':10,'IX':9,
                 'L':50,'C':100,'XL':40,'XC':90,
                 'D':500,'M':1000,'CD':400,'CM':900}
        value=0
        
        l=len(s)
        i=0
        while i<l:
            if  i+1!=l:
                if  s[i]+s[i+1] in vals:
                    value+=vals[s[i]+s[i+1]]
                    i+=2
                    continue
            value+=vals[s[i]]
            i+=1
        return value    

                           