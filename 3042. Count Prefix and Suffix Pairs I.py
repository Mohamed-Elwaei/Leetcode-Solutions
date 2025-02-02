class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        def helper(a, b):
            if len(a) > len(b): return False
            
            return b[:len(a)] == a and b[-len(a):] == a
        
        
        
        count = 0
        n = len(words)
        for i in range(n):
            for j in range(i+1,n):
                
                count += helper(words[i],words[j])
        return count