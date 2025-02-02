"""
cardPoints = [1,2,3,4,5,6,1], k = 3


we can take [1,2,3] from the left and [] from the right
we can take [1,2] from the left and [1] from the right
we can take [1] from the left and [6,1] from the right
we can take [] from the left and [5,6,1] from the right


cardPoints = [9,7,7,9,7,7,9], k = 4

we can take [9,7,7,9] from the left and [] from the right.




"""

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)

        if k >= n:
            return sum(cardPoints)

        
        left = sum(cardPoints[:k])
        right = 0
        answer = left
        
        for i in range(k):
            left -= cardPoints[k - 1 - i]

            right += cardPoints[n - 1 - i]
            answer = max(answer, right + left)
        return answer