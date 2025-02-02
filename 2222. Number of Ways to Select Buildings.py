"""
We will have 3 2-tuples: ones, twos, threes.

ones[0] will be how many valid subsequences end with 0 of size one.
ones[1] will be how many valid subsequences end with 1 of size one.

twos[0] will be how many valid subsequences end with 0 of size two.
twos[1] will be how many valid subsequences end with 1 of size two.

threes[0] will be how many valid subsequences end with 0 of size three.
threes[1] will be how many valid subsequences end with 1 of size three.


for i in s.
    ones[i] += 1
    twos[i] += ones[i^1]
    threes[i] += twos[i^1].

ones = (3,3)
twos = (2,7)
threes = (4,2)
s = '001101'


"""

class Solution:
    def numberOfWays(self, s: str) -> int:
        
        ones = [0,0]
        twos = [0,0]
        threes = [0,0]

        for c in s:
            i = int(c)
            ones[i] += 1
            twos[i] += ones[i^1]
            threes[i] += twos[i^1]
        return sum(threes)