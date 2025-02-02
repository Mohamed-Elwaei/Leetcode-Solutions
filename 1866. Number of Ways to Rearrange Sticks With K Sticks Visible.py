"""
if n == k, answer is 1
if k == 1 answer is (n-1)!.


We need stick n (largest stick) to be at least at position k (1-indexed).
If stick n was positioned at index i, 
then there are (n-1)P(n-i) permutations at the back of stick i.
At the front the problem simplifies to k = k - 1 and n = n - (n - i - 1).


If stick n was at index i (0-indexed),
then there are (n-1)P(n-i-1) permutations at the back of stick i.
At the front the problem simplifies to k = k - 1 and n = i.
"""
max_n = int(30)
factorials = [1] * max_n
m = int(1e9 + 7)

for i in range(2,max_n):
    factorials[i] = i * factorials[i-1] % m


def inverse(a):
    return pow(a,m-2,m)

def P(n,k):
    return (factorials[n] * inverse(factorials[n-k])) % m


class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        
        memo = {}

        def F(n,k):

            
            if (n,k) in memo:
                return memo[n, k]
            
            if k == n: 
                memo[n,k] = 1

            if k == 1:
                return factorials[n - 1]
            memo[n, k] = 0
            for i in range(k,n):
                memo[n,k] = (memo[n, k] + (P(n-1, n - i - 1) * F(i, k - 1)) % m) % m

            return memo[n, k]
        
        return F(n,k-1)
    

s = Solution()

print(s.rearrangeSticks(n=3,k=2))