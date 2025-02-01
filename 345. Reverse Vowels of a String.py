class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        stack=[]
        snew=[]
        for i,l in enumerate(s):
            if l in vowels:
                stack.append(i)
            snew.append(l)   

        l=0
        r=len(stack)-1
        
        while l<r:
            snew[stack[l]],snew[stack[r]]=snew[stack[r]],snew[stack[l]]
            l+=1
            r-=1        
        return ''.join(snew)  