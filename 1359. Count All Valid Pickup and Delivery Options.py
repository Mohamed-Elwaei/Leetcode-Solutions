"""
At all indices in the sequence or array, we cannot have more deliveries than pickups.
Which means that we have an upper bound of catalan numbers.

Our answer must be less than or equal to (2n)Cn - (2n)C(n+1).

Our array is size 2n.
Let's say we start out with an empty array.

We have 2n choices for P1. Lets say we chose index i.
Then for D1 we have (2n - (i + 1)) choices.
Then we have to solve for F(n-1).


def F(n):
    if n == 1:
        return 1

    For i from range 0 to 2n:
        ans *= (2n - (i + 1)) * F(n-1)



"""



m = int(1e9 + 7)

class Solution:
    def countOrders(self, n: int) -> int:
        prev = 1
        next = 0

        def F(n):
            nonlocal prev, next
            next = 0
            for i in range(0,2*n):
                next = (next + (2*n - (i + 1)) * prev) % m

        for i in range(2,n+1):
            F(i)
            prev = next
        return prev