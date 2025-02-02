

class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        

        perms = []
        perm = []
        def F():
            if len(perm) == 4:
                perms.append([arr[i] for i in perm])
                return
            
            for i in range(4):
                if i not in perm:
                    perm.append(i)
                    F()
                    perm.pop()
        F()
        ans = None
        for p in perms:

            if (10*p[0] + p[1] < 24) and (10*p[2] + p[3] < 60):
                p = [str(i) for i in p]
                if ans == None:
                    ans = ''.join(p)
                else:
                    ans = max(ans, ''.join(p))

        
        if ans == None:
            return ''

        return f'{ans[0]}{ans[1]}:{ans[2]}{ans[3]}'