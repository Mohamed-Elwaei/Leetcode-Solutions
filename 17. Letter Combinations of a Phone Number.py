class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        map = ['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        combinations = []
        path = []
        def dfs(i):
            if i >= len(digits): 
                if path:
                    combinations.append(''.join(path))
                return    
            
            digit = int(digits[i])
            for letter in map[digit]:
                path.append(letter)
                dfs(i+1)
                path.pop()
        dfs(0)
        return combinations