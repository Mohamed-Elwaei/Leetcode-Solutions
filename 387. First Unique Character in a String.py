class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency = [0] * 26 #Key => Ocurrences
        for c in s: 
            frequency[ord(c) - ord('a')] += 1
        
        for i,c in enumerate(s): 
            if frequency[ord(c) - ord('a')] == 1:
                return i
        return -1
        #Time complexity: O(2n) => O(n)
        #Memory complexity O(1)