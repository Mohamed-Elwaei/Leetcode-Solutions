class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l,r = 0,k
        num = 0
        vowels = 'aeiou'
        for c in range(r):
            if s[c] in vowels:
                num+=1
        currnum = num
        while r<len(s):
            if s[l] in vowels:
                currnum-=1
            if s[r] in vowels:
                currnum+=1
            num = max(num,currnum)
            l,r = l+1,r+1
        num = max(num,currnum)
        return num