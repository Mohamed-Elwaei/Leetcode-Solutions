"""
customers = [1,0,1,2,1,1,7,5], 
grumpy =    [0,1,0,1,0,1,0,1], 
minutes = 3

2 pointer technique in linear time. (SLiding window)

In the next iteration, if our window is more that minutes long, we shrink from the left.
We update accordingly.

First calculate sum of satisfied customers, calculate sum of disatisfied customers.
Pick the least amount of disatisfied customers given the optimal window. Subtract from the satisfied customers.
"""

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied = disatisfied = 0

        n = len(customers)
        for i in range(n):
            satisfied += customers[i]
            disatisfied += customers[i] * grumpy[i]

        
        #We then pick the optimal window.
        l = 0
        tmp = 0
        bestWindow = 0
        for r in range(n):
            tmp += customers[r] * grumpy[r]

            if r - l + 1 > minutes:
                tmp -= customers[l] * grumpy[l]
                l += 1
            bestWindow = max(tmp, bestWindow)
        
        disatisfied -= bestWindow
        satisfied -= disatisfied
        return satisfied