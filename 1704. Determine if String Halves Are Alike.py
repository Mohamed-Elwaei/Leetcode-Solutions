class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l,r = 0,len(s)-1
        vowels = 0
        while l<r:
            if s[l] in 'aeiouAEIOU':
                vowels+=1
            if s[r] in  'aeiouAEIOU':
                vowels-=1
            l+=1
            r-=1
        return not vowels

        