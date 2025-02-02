class Solution(object):
    def countVowelStrings(self, n):
        """
        :type n: int
        :rtype: int
        """
        def dfs(n):
            if n == 1:
                return ['a','e','i','o','u']
            
            combs=dfs(n-1)
            ret = []

            for c in combs:
                for v in ['a','e','i','o','u']:
                    if ord(v)<=ord(c[-1]) :
                        ret.append(c+v)
            return ret
        
        ans = dfs(n)
        return len(ans)