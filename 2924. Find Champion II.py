"""
Each node is a team.

An edge (u,v) is a directed edge from u to v meaning team u is stronger than team v.

There exists a champion if there is only one node with an in degree of 0.

Proof:
2 cases where there are no unique champions.

1. If there are no nodes with an indegree of 0. That means we have a cycle.
2. If there is more than one node with an indegree of 0.

"""
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegrees = [0] * n

        for _, v in edges:
            indegrees[v] += 1
        
        answer = -1

        for node in range(n):
            if indegrees[node] == 0:
                if answer == -1: answer = node
                else: return -1
        return answer