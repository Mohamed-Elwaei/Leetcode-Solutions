
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = dict()
        for i,(num,den) in enumerate(equations):
            if num not in graph:
                graph[num] = [(den,values[i])]
            else:
                graph[num].append((den,values[i]))
            if den not in graph:
                graph[den] = [(num,1/values[i])]
            else:
                graph[den].append((num,1/values[i]))
        solutions = []
        print(graph)

        def dfs(num,den,curr = 1.0):
            if num not in graph or den not in graph:
                return -1.0
            if num==den:
                return curr*1.0
            visited.add(num)
            for nxt,val in graph[num]:
                if nxt not in visited:
                    tmp = dfs(nxt,den,curr*val)
                    if tmp!=-1.0:
                        return tmp
            return -1.0
        
        for num,den in queries:
            visited = set()

            solutions.append(max(dfs(num,den),dfs(den,num)))
        return solutions


                
             
            

                