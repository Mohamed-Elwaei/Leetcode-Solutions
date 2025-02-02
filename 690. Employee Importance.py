"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = {}
        for e in employees:
            graph[e.id] = [e.subordinates, e.importance]
        
        ans = 0
        def dfs(e):
            nonlocal ans
            ans += graph[e][1]

            for subs in graph[e][0]:
                dfs(subs)
        dfs(id)
        return ans