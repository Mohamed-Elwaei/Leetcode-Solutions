"""
Use rabin karp string matching algorithm to get all 10-letter-long substrings
that occur more than once.

rabin karp uses a rolling hash function.

0000011111
AAAAACCCCC
"""


ord = lambda x : {"A":1,'C':2,'G':3,'T':4}[x]


M = int(1e10)

def rabinKarp(s):
    S = set()
    ans = set()

    h = 0

    for i in range(len(s)):
        h = (h*10 + ord(s[i])) % M

        print(s[max(0,i-9):i+1], " hashes to ", h)
        if h in S:
            ans.add(s[max(0,i-9):i+1])
        if i >= 9:
            S.add(h)
    
    return ans

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        return rabinKarp(s)