def partition( s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        palis = []
        i = 0
        curr = []
        def dfs(i):
            if i==len(s):
                palis.append(curr[:])


            for j in range(i,len(s)):
                l,r = j,j
                while l>-1 and r<len(s) and s[l]==s[r]:
                    curr.append(s[l:r])
                    dfs(r)
                    curr.pop()
                    l-=1
                    r+=1
        dfs(0)
        return palis

print(partition('aab'))