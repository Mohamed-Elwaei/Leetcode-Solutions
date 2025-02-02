"""
We say that word is k-periodic if there is some string s of length k such that word can be obtained by concatenating s an arbitrary number of times.


word = "leetcodeleet", k = 4

In this example s can be 'leet' or 'code'. 'leet' occurs 2/3 times, while 'code' occurs 1/3. So it's easier to fill the string with leet.



word = "leetcoleet", k = 2

In this example s can be 'le','et', or 'co'. 'le' occurs 2/5 times, co occurs 1/5 times, 'et' occurs 2/5 times

leetcoleet
lelecoleet
leleleleet
lelelelele


So just make the greedy choice and pick the candidate that occurs most often.
"""

from collections import defaultdict
class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        
        n = len(word)
        
        counter = defaultdict(int)
        
        for i in range(0,n,k):
            counter[word[i:i+k]] += 1
        
        ans = n
        
        for _,val in counter.items():
            ans = min(ans, n//k - val)
        return ans
        