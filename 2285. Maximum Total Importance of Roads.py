"""
We want to maximize the importance.

We add each integer x number of times where is the degree of the node it is assigned to.

Let's start with the largest integer.
We want to add that no. the largest amount of time. We assign it the node with the most edges.


Greedy choice: Assign the largest no.s with the nodes with the most degrees.

Solution:
Count the degrees for each node.
Sort the nodes by degrees in ascending order.

degrees is one indexed here.
For i in range [1,n]:
    answer += degrees[i] * i
"""

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for u,v in roads:
            degrees[u]+=1
            degrees[v]+=1
        answer = 0
        degrees.sort()

        for i in range(1,n+1):
            answer += degrees[i-1] * i
        return answer