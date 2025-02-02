class Solution:
    def isThree(self, num: int) -> bool:
        divisors = 2
        n = 2
        while n*2 <= num:
            if num % n == 0:
                divisors += 1
            n+=1
        print(divisors)
        return divisors == 3