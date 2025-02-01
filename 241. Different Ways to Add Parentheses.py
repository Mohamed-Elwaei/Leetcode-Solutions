def diffWaysToCompute( expression: str) -> list[int]:
        values = set()
        opens,closed = [0],[0]

        def dfs(curr, i):
            if i>=len(expression):
                for _ in range(closed[0],opens[0]):
                    curr+=')'
                
                values.add(eval(curr))
                return 

            if expression[i] in '-+*':
                if opens[0]>closed[0]:
                    closed[0]+=1
                    dfs(curr + ')' + expression[i],i+1)
                    closed[0]-=1
                dfs(curr + expression[i],i+1)
            
            num = ''
            while i < len(expression) and expression[i] in '0123456789':
                num+=expression[i]
                i+=1
            
            if opens[0]>closed[0]:
                closed[0] += 1
                dfs(curr  + num + ')', i)
                closed[0] -= 1
            opens[0] += 1
            dfs(curr + '(' + num, i)
            opens[0] -= 1
        dfs('',0) 
        return values


print(diffWaysToCompute("2-1-1"))