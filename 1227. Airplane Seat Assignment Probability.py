"""

Regardless of the outcomes, there are n-1 seats left.


If the first passenger picks the correct seat, That occurs with probablity 1/n. 
Minimum answer is 1//n.
If the first passenger picks the nth seat. That also occurs with probability 1/n.


So focus on the range [2,n-1]. Thats n-2.

If n == 1: return 1
If n == 2: return 0.5

If the first passenger picks a seat in range [2,n-1]. He has n-2 seats to sit in

Second passenger has n-3 seats.
Third has n-4



We will focus on the probability the nth passenger does not get his own seat.

Let A be the event the nth passenger does not get his own seat.


P(A) = P(first picks n) + P(first does not pick n and second picks n) + P(first and second do not pick n and third does pick n)

Answer = 1 - P(A).


"""



class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        return 1.0 if n == 1 else 0.5