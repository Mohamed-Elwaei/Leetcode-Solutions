class Solution:
    def minSteps(self, s: str, t: str) -> int:
        """
        1 <= N <= 2 * 10^5

        s = {
            l:1
            e:3
            t:1
            c:1
            o:1
            d:1
        }
        t = {
            c:1
            o:1
            a:1
            t:1
            s:1
        }
        add 1 l, 3 e's, 1 d, 
        add 1 a, s
        """

        a = {}   #Map each letter to occurences in s
        b = {}   #Map each letter to occurences in t

        for c in s:
            a[c] = a.get(c,0) + 1
        for c in t:
            b[c] = b.get(c,0) + 1
        
        answer = 0
        for c in a:
            answer += max(0, a[c] - b.get(c,0))
        
        for c in b:
            answer += max(0, b[c] - a.get(c,0))
        return answer
        