class Solution:
    def canCross(self, stones: List[int]) -> bool:
        memo = set()
        def dfs(pos,k):
            if pos==max(stones):
                return True
            if (pos,k) in memo:
                return False
            if pos not in stones:
                return False
            memo.add((pos,k))
            
            jumps = set([max(k-1,1),k,k+1])

            for jump in jumps:
                if dfs(pos+jump,jump):
                    return True
            return False
        return dfs(1,1)