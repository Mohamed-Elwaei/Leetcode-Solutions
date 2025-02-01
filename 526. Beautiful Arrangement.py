"""

Let's say we have n numbers.

Then we have n numbers to choose from for index n.
Then we remove the number chosen and the problem simplifies to n-1.

The dimensions would be n and what numbers are available.
numbers available can be represented as an integer.
If the ith bit in the integer is set then the ith bit is available.


F(n, numbers available):
    answer = 0
    for every number x available:
        if x % n == 0 or n % x == 0:
            answer += F(n-1, numbers available except x)
"""

max_n = 16
DP = [0] * max_n
DP[1] = 1


memo = {}

#returns how many beautiful arrangements of size size given the numbers available
def F(size: int, numbers_available: int): 
    if size == 0:
        return 1
    state = (size, numbers_available)

    if state in memo:
        return memo[state]
    
    memo[state] = 0

    for i in range(max_n):
        if (numbers_available >> i) & 1 == 0 or (size % i != 0 and i % size != 0):
            continue
        memo[state] += F(size-1, numbers_available ^ (1 << i))

    return memo[state]

numbers_available = 0

for n in range(1, max_n):
    numbers_available |= (1 << n)
    DP[n] = F(n, numbers_available)

class Solution:
    def countArrangement(self, n: int) -> int:
        return DP[n]