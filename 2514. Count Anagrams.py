"""

for a word with n letters

let letters a,b,c,....,z occur with frequencies f1,f2,f3,...,f26.

answer = 1

for f in f1,f2,f3...f26:
    answer = nCf * answer
    n -= f



s = "too hot"

[too, hot]

too has 3C2 * 1C1 anagrams
hot has 3C1 * 2C1 * 1C1 anagrams

product is 18.



C(n,k) = n! / ((n-k)! * k!) % m
       = n! * ((n-k)!)^(-1) * (k!)^(-1) % m.

a^(p-1) = 1 mod m if p is a prime.
meaning a^(p-2) is our modular inverse.
"""

max_n = int(1e5 + 1)
m = int(1e9 + 7)

factorials = [0] * max_n

factorials[0] = 1

for i in range(1,max_n):
    factorials[i] = (factorials[i - 1] * i) % m


def inverse(a):
    return pow(a,m-2,m)


def C(n,k):
    return factorials[n] * (inverse(factorials[n-k]) * inverse(factorials[k]) % m) % m

class Solution:
    def countAnagrams(self, s: str) -> int:
        words = s.split()


        ans = 1
        
        for w in words:
            letters = [0] * 26
            for l in w:
                letters[ord(l) - ord('a')] += 1
            
            n = len(w)
            for k in letters:
                ans = (ans * C(n,k)) % m
                n -= k
        return ans

