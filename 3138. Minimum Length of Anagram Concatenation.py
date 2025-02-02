"""
n = len(s)

If n is a prime no. then the answer is n.
If s consists of 1 letter, the answer is 1.


One options is to look at all the factors of n. Then iterate over the factors in increasing order.
For each factor f:
    check the occurences of all characters c:
    
    for each occurrence for a character c:
      check if n/f divides the occurrence.


s = "abba"
ab (2) is t.

s = 'abbc'
abbc (2) is t.


s = 'abbbbbba'
abbbbbba is minimum t.


s = 15 character string

3 a's 3 b's 3 c's 3 d's 3 e's
t would be abcde

6 a's 3 b's 3 c's 3 d's 
t would be aabcd (5)

5 a's 5 b's 5 c's

t would be abc.
"""


def divisors(n):
    ret = [1,n]
    
    i = 2
    
    while i*i <= n:
        
        if n % i == 0:
            ret.append(i)
            ret.append(n//i)
        i+=1
    
    ret.sort()
    return ret

from collections import Counter, defaultdict
class Solution:
    def minAnagramLength(self, s: str) -> int:
        
        n = len(s)
        factors = divisors(n)
        print(factors)
        
        frequencies = Counter(s)
        for f in factors:
            
            flag = 0
            
            anagram = defaultdict(int)
            for letter,o in frequencies.items():
                if o % (n//f) != 0:
                    flag = 1
                    break
                else:
                    anagram[letter] = o // (n // f)
            if flag != 0:
                continue
            
            for i in range(0,n,f):
                tmp = defaultdict(int)
                for c in s[i:i+f]:
                    tmp[c]+=1
                
                for c in tmp:
                    if tmp[c] != anagram[c]:
                        flag = 1
                        break
            if flag != 0:
                continue
            
            return f
        
                