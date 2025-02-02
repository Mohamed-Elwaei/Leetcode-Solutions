import string
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        #s = "aba", t = "baba"
        #For s: 'a':2 'b':1 'ab':1 'ba':1
        #For t: 'a':2 'b':2  'ab':1 'ba':2
        # answer = 'a' from s * 'b' from t + 'b' from s * 'a' from t
        #If s and t consist of entirely different letters, then our answer is M*N where M and N are
        #Both substrings have to be the same length.
        # 1 <= M <= 100
        # 1 <= N <= 100
        # Only lowercase letters are used.

        #We will map all substrings in t with their frequency
        if len(s) > len(t):
            s,t = t,s

        M,N = len(s), len(t)

        freqT = {}
        
        for i in range(N):
            tmp = ''
            for j in range(i,N):
                tmp += t[j]
                freqT[tmp] = freqT.get(tmp, 0) + 1
        
        freqS = {}
        for i in range(M):
            tmp = ''
            for j in range(i,M):
                tmp += s[j]
                freqS[tmp] = freqS.get(tmp, 0) + 1
        
        answer = 0
        # print(freqS,'\n', freqT)
        for strS in freqS: #O(M^2)
            for i in range(len(strS)): #O(M)
                for c in string.ascii_lowercase: #O(26)
                    if c == strS[i]: continue
                    strT = strS[:i] + c + strS[i + 1:]
                    if strT in freqT:
                        # print(strS,strT)
                        answer += freqT[strT] * freqS[strS]
        return answer

        #O(M^2 + N^2) memory complexity
        #O(26 * M^3) => O(M^3) for time complexity
