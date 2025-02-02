from typing import List

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        children = [0] * k
        answer = float('inf')
    
        def dfs(index):
            nonlocal answer

            if index == n:
                answer = min(answer, max(children))
                return
            
            for i in range(k):
                children[i] += cookies[index]
                if children[i] < answer:
                    dfs(index + 1)
                children[i] -= cookies[index]
        cookies.sort(reverse=True)
        dfs(0)
        return answer