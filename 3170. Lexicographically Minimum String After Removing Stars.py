"""
s = "axabac*"

delete third a to get axabc

if we delete second a we get axbac
if we delete first a we get xabac


s = "abacax*"


if we delete first a we get bacax
if we delete second a we get abcax
if we delete third a we get abacx


s = "axacab*"

if we delete first a we get xacab
if we delete second a we get axcab
if we delete third a we get axacb

Make a greedy choice and delete the rightmost element.


"""
import heapq
class Solution:
    def clearStars(self, s: str) -> str:
        
        toRemove = set()
        heap = []
        n = len(s)
        for i in range(n):
            
            if s[i] == '*':
                toRemove.add(-heapq.heappop(heap)[1])
            else:
                heapq.heappush(heap, [s[i], -i])
        
            
        ans = ''
        
        for i in range(n):
            if i not in toRemove and s[i] != '*':
                ans += s[i]
        return ans
        
            
            
        