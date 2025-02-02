
"""
we create two auxillary arrays of size n: left and right where n is the size of the array.


let left[i] be the closest distance to the person sitting on the left.
let right[i] be the closest distance to the person sitting on the right.


the answer would be the min(left[i],right[i]) maximised for all i in range[0,n-1]

"""

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        left = [0] * n
        right = [0] * n
        
        left[0] = right[n-1] = float('inf')
        if seats[0]:
            left[0] = 0
        if seats[n-1]:
            right[n-1] = 0
            
        for i in range(1,n):
            if seats[i]:
                left[i] = 0
            else:
                left[i] = left[i-1] + 1
        
        for i in range(n-2,-1,-1):
            if seats[i]:
                right[i] = 0
            else:
                right[i] = right[i+1] + 1
        
        answer = 0
        print(left)
        print(right)
        for i in range(n):
            answer = max(answer, min(left[i], right[i]))
        return answer