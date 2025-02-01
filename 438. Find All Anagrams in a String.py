"""
Solution would be using a sliding window and a hashmap. O(26 * n) in time complexity.

Hash all the letters in p to their frequencies.
Hash all the letters in the sliding window to the frequencies.

Check how many times the sliding window hashmap is the same as p's hashmap.
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash_p = {c:0 for c in string.ascii_lowercase}
        hash_window = {c:0 for c in string.ascii_lowercase}

        for c in p:
            hash_p[c]+=1

        n = len(s)
        m = len(p)
        l = 0

        answer = []
        for r in range(n):
            hash_window[s[r]] += 1

            if r - l + 1 > m:
                hash_window[s[l]] -= 1
                l += 1
            
            valid = 1

            for c in string.ascii_lowercase:
                if hash_window[c] != hash_p[c]:
                    valid = 0
                    break
            
            if valid == 1:
                answer.append(l)
        return answer
