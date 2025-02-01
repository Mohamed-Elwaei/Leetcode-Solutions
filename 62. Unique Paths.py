class Solution(object):
    def aux(self,m,n,ways):
        key=tuple((m,n))
        if ways[key]!=-1:
            return ways[key]
        if m==0 or n==0: return 0
        if m==1 or n==1: return 1
        
        ways[key]=self.aux(m,n-1,ways)+self.aux(m-1,n,ways)
        return ways[key]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        ways=defaultdict(lambda:-1)
        return self.aux(m,n,ways)