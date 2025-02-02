class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        
        def helper(x):
            return ord(x) - ord('a')
        s = [helper(c) for c in s]
        
        
        for i in range(len(s)):
            # print(s,k)
            if s[i] + k > 25 and s[i] - k <= 0:
                k -= min(26 - s[i], s[i])
                s[i] = 0
                
            elif s[i] - k <= 0:
                k -= s[i]
                s[i] = 0
            elif s[i] + k > 25:
                k -= 26 - s[i]
                s[i] = 0
            else:
                s[i] -= k
                k = 0
        s = [x + ord('a') for x in s]
        s = [chr(x) for x in s]
        return ''.join(s)