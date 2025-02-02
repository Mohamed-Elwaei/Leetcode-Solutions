"""
We want all numbers in tops or bottoms to be the same.
We know that 1 <= tops[i] <= 6.

We use a Function F.
F takes parameters, A,B, X.

F(A,B,X) returns true if we can make all numbers in A equal to X by swapping one or more A[i] with B[i].

We do 12 passes of F(A,B,X).
One for each X in [1,6].
And One for each side.


"""


def F(A,B,x):

    rotations = 0
    for a,b in zip(A,B):
        if a == x: 
            continue
        if b == x:
            rotations += 1
        else:
            return float('inf')
    return rotations

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        ans = float('inf')

        for i in range(1,7):
            ans = min(F(tops,bottoms,i), F(bottoms,tops,i), ans)
        
        if ans == float('inf'):
            return -1
        return ans