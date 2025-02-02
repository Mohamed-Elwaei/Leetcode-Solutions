"""
We can use a modified version of Djikstra.

But we have to keep track of the discounts.

We would use a 2D matrix, call it dp. The dimensions would be the nodes and discounts used.

dp[i][j] is the minimum distance from node 0 to node j using i discounts.

As we process all the edges in the node in djikstra, we have two choices.

choice 1: Use a discount

choice 2: Do not use a discount.
"""

import heapq



class Solution:
    def minimumCost(self, n: int, highways, discounts: int) -> int:
        V, E = n, len(highways)
        graph = [[] for _ in range(V)]
        for u,v,w in highways:
            graph[u].append((v,w))
            graph[v].append((u,w))


        DP = []
        processed = []


        for _ in range(discounts+1):
            DP.append([float('inf')] * V)
            processed.append([False] * V)
            DP[-1][0] = 0



        def Djikstra(discounts):
            start = 0
            heap = [(0,0,start)] #Heap consists of a 3-tuple: discounts used, distance, node 

            
            while heap:
                discounts_used, distance, node = heapq.heappop(heap)

                if processed[discounts_used][node]: continue
                processed[discounts_used][node] = True

                for neigh, weight in graph[node]:
                    if distance + weight < DP[discounts_used][neigh]:
                        DP[discounts_used][neigh] = distance + weight
                        heapq.heappush(heap, (discounts_used, DP[discounts_used][neigh], neigh))

                    
                    if discounts_used < discounts and distance + weight//2 < DP[discounts_used + 1][neigh]:
                        DP[discounts_used + 1][neigh] = distance + weight//2
                        heapq.heappush(heap, (discounts_used + 1, DP[discounts_used + 1][neigh], neigh))
        
        Djikstra(discounts)

        answer = float('inf')
        for row in DP:
            answer = min(answer, row[-1])
        if answer == float('inf'):
            return -1
        return answer
        
        



s = Solution()

print(s.minimumCost(n = 4, highways = [[1,3,17],[1,2,7],[3,2,5],[0,1,6],[3,0,20]], discounts = 20))