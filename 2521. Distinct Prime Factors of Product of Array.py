"""
We can't just multiply all the elements and run euler totient.
Because we can run into overflow.

We have a solution that is O(n*sqrt(n))

"""


class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        factors = set()

        def factorize(n):
            print(n, "Start")
            i = 2
            while i*i <= n:
                count = 0
                while n % i == 0:
                    count += 1
                    n //= i


                if count != 0:
                    factors.add(i)
                i+=1
            
            if n != 1:
                factors.add(n)

        for n in nums:
            factorize(n)
        return len(factors)