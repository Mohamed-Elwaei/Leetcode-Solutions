class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        ans = [float('inf')]
        visited = set()
        path = []
        def dfs(start,end):
            visited.add(start)
            path.append(start)

            if start == end:
                ans[0] = min(ans[0],len(path)-1)
            else:
                for i in range(len(start)):
                    for c in 'ACGT':
                        nxt = start[:i] + c + start[i+1:]
                        if nxt not in visited and nxt in bank:
                            dfs(nxt,end)
            visited.remove(start)
            path.pop()
        dfs(startGene,endGene)
        print(path)
        return ans[0] if ans[0] != float('inf') else -1            
