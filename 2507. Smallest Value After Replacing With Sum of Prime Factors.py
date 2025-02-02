



def sumOfPrimeFactors(n):
    sum = 0

    i = 2

    while i*i <= n:
        
        count = 0
        while n % i == 0:
            count += 1
            n //= i
        
        if count != 0:
            sum += i * count
        i += 1
    
    if n != 1:
        sum += n
    return sum




class Solution:
    def smallestValue(self, n: int) -> int:
        
        next = sumOfPrimeFactors(n) 

        while next != n:
            n = next
            next = sumOfPrimeFactors(n)
        return n