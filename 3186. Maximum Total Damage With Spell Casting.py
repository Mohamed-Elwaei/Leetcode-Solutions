"""

Sort the array.
[7,1,6,6]


   [1,6,6,7]

dp=[1,7,13,13]

let dp[i] be the maximum damage with array power[0..i]


 
   [1,1,3,4]
dp=[1,2,5,6]


dp[i] = 
{
 dp[i-1] + power[i] if power[i] == power[i-1] or power[i-1] < power[i] - 2

 dp[j] + power[i] where j is the largest index of a number n where n < power[i] - 2
}



[7,1,6,3]

[1,3,6,7]

[1,3,9,10]
"""

from collections import Counter
class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        counter = Counter(power)
        
        power = list(counter.items()) #power is an array of tuples, each tuple contains a no. and it's occurences.
        
        power.sort()
        print(power)
        n = len(power)
        dp = [0] * n
        
        dp[0] = power[0][0] * power[0][1]
        
        for i in range(1,n):
            j = i
            while j >= 0 and power[i][0] - power[j][0] <= 2:
                j-=1
            
            if j != -1:
                dp[i] = max(dp[j] + power[i][0] * power[i][1], dp[i-1])
            else:
                dp[i] = max(power[i][0] * power[i][1], dp[i-1])
        return dp[-1]
        
        