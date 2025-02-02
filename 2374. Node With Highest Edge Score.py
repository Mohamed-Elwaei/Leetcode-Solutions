class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        V = E = len(edges)
        scores = {i:0 for i in range(V)}

        for i in range(V):
            scores[edges[i]] += i

        
        ans = 0

        for node in scores:
            if scores[node] > scores[ans]:
                ans = node
        return ans