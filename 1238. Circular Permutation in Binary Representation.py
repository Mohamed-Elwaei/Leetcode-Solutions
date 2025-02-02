class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        perm = []
        visited = set()
        def check(a,b):
            diffs = 0
            for i in range(n):
                bita = (1 << i) & a
                bitb = (1 << i) & b
                if bita ^ bitb == 0: continue
                diffs += 1
            return diffs == 1

        def dfs(curr):
            if len(perm) == 2**n and check(perm[-1],perm[0]): 
                return True

            if curr in visited:
                return False

            visited.add(curr)
            perm.append(curr)
            for i in range(n):
                copy = curr
                copy ^= (1 << i)
                if dfs(copy):
                    return True
            perm.pop()
            visited.remove(curr)
            return False
        dfs(start)
        return perm