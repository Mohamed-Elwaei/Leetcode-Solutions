class Solution:
    def sortVowels(self, s: str) -> str:
        s = [c for c in s]
        vowels = 'aeiouAEIOU'

        vowels2 = []

        for c in s:
            if c in vowels:
                vowels2.append(c)
        vowels2.sort()
        j = 0

        for i in range(len(s)):
            if s[i] in vowels:
                s[i] = vowels2[j]
                j+=1
        return ''.join(s)

        