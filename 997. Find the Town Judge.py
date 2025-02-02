class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ins =  {i:0 for i in range(1,n+1)}
        outs = {i:0 for i in range(1,n+1)}

        for u,v in trust:
            ins[v] += 1
            outs[u] += 1
        
        judge = None
        for node in outs:
            if outs[node] == 0 and judge == None:
                judge = node
            elif outs[node] == 0:
                return -1
        
        if not judge or ins[judge] != n - 1: return -1
        return judge

        