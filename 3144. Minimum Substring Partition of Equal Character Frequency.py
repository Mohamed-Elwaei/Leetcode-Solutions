class Solution:
    def minimumSubstringsInPartition(self, s: str) -> int:
        
        n = len(s)
        dp = [i+1 for i in range(n)] #dp[i] is the minimum no. of partitions for substring s[0..i]
        
        def balanced():
            num = -1
            for i in range(26):
                if freq[i] == 0: continue
                    
                if num == -1: 
                    num = freq[i]
                if freq[i] != num:
                    return False
            return True
                
                    
        
        for i in range(n):
            
            freq = [0] * 26
            for j in range(i,n):
                freq[ord(s[j]) - ord('a')]+=1
                
                if balanced():
                    
                    if i > 0:
                        dp[j] = min(dp[j], dp[i-1] + 1)
                    else:
                        dp[j] = 1
        
        return dp[n-1]