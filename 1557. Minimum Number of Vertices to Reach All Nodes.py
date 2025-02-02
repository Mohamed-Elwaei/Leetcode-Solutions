class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ins = {i:0 for i in range(n)}
        for _,v in edges:
            ins[v] += 1
        return [v for v in ins if ins[v] == 0]