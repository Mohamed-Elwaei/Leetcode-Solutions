def z_algo(s):
    n,l,r = len(s),0,0

    z = [0] * n

    for i in range(1,n):
        if i < r:
            z[i] = min(r-i, z[i - l])
        
        while i + z[i] < n and s[z[i]] == s[z[i]+i]:
            z[i] +=1
        if i+z[i] > r:
            l,r = i,i+z[i]
    return z 

def longestPrefix(s: str) -> str:

        z = z_algo(s)
        longest = 0

        for i in range(len(z)-1,-1,-1):
            if z[i] + i == len(z):
                longest = max(z[i],longest)
        
        return s[len(s) - longest:]

s="ababab"
print(longestPrefix(s))