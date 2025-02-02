"""
We calculate the score of each student and rank them.
"""

import heapq

class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        P = set(positive_feedback)
        N = set(negative_feedback)
        
        def F(report: str) -> int: #Calculate the points for the given report.
            words = report.split()
            
            score = 0
            for w in words:
                if w in P:
                    score += 3
                elif w in N:
                    score -= 1
            return score
        
        
        heap = [] #Rank the students
        
        
        for r, ID in zip(report, student_id):
            score = F(r)
            
            heapq.heappush(heap, (-score, ID))
        
        ans = []
        
        for _ in range(k): #Get the top k students:
            _,ID = heapq.heappop(heap)
            
            ans.append(ID)
        return ans