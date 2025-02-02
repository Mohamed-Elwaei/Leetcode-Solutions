class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        answer = 0

        vowels = 'aeiou'
        n = len(s)
        for i in range(n):
            v = c = 0
            for j in range(i,n):
                if s[j] in vowels:
                    v += 1
                else:
                    c += 1

                if v == c and (v*c) % k == 0:
                    answer += 1
        return answer