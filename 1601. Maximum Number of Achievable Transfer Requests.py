from collections import defaultdict
class Solution:
    def maximumRequests(self, n: int, requests: list[list[int]]) -> int:
        graph = {b: defaultdict(int) for b in range(n)}

        for u,v in requests:
            graph[u][v] += 1
        
        def dfs(path,visited):
            nonlocal longest
            u = path[-1]
            if u in visited:
                if len(path) > len(longest):
                    longest = path[:]
                return
            visited.add(u)
            for v,w in graph[u].items():
                if w<=0: continue
                dfs(path + [v], visited)

        answer = 0
        cycles = True
        while cycles:
            cycles = False
            for v in range(n):
                longest = []
                dfs([v],set())
                if not longest: continue
                cycles = True
                last = longest[-1]
                start = len(longest) - 2
                while longest[start] != last:
                    graph[longest[start]][longest[start] + 1] -= 1
                    answer += 1
                    start -= 1
                graph[longest[start]][longest[start+1]] -= 1
                answer += 1
        return answer

s = Solution()
print(s.maximumRequests(n = 3, requests = [[0,0],[1,2],[2,1]]))