

max_n = int(1e6+1)
sieve = [0] * max_n
sieve[1] = 1

for i in range(2,max_n):
    
    j = i + i
    while j < max_n:
        sieve[j] = i
        j += i
    
def prime(num):
    return sieve[num] == 0

class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:
        
        freq = {} #Maps each number to its occurrences.
        
        directions = [[-1,0],[1,0],[0,1],[0,-1],[1,1],[1,-1],[-1,1],[-1,-1]]
        
        def dfs(r,c,dr,dc):
            num = 0
            
            while 0 <= r < n and 0 <= c < m:
                
                num = (num * 10) + mat[r][c]
                if prime(num) and num > 10:
                    freq[num] = freq.get(num,0) + 1
                
                r += dr
                c += dc
            
            
            
        
        n,m = len(mat), len(mat[0])
        
        
        for r in range(n):
            for c in range(m):
                
                for d in directions:
                    
                    dfs(r,c,d[0],d[1])
                
                
        
        order = [(v,k) for (k,v) in freq.items()]
        
        order.sort(reverse = True)
        
        print(order)
        for _, num in order:
            return num
        return -1