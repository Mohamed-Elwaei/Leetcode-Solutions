"""
This is a directed acyclic graph.
Each edge (u,v) means person v is richer than person u.
The solution would be a dfs.
Keep track of visited nodes, in order to not wast recomputation time

If node x has no out degrees then answer[x] = x.
otherwise answer x will be the min(answer[x], answer[c1], answer[c2], ... answer[ck]) where there is an 
edge (x, ci) for all i from 1 to k.


"""
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        V, E = len(quiet), len(richer)
        answer = [-1] * V #if answer[i] == -1, then node i has not been visited in the dfs yet
        graph = [[] for _ in range(V)]

        for a,b in richer:
            graph[b].append(a)
        

        def dfs(u): #dfs function will return the minimum quietness in node u's tree.

            if answer[u] != -1:
                return answer[u]
            answer[u] = u


            for v in graph[u]:
                res = dfs(v)
                if quiet[res] < quiet[answer[u]]:
                    answer[u] = res

            return answer[u]
        

        for node in range(V):
            dfs(node)
        
        return answer