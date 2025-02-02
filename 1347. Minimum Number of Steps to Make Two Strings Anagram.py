class Solution:
    def minSteps(self, s: str, t: str) -> int:

        one,two = [0]*26, [0] * 26
        for c in s:
            one[ord(c) - ord('a')] +=1
        for c in t:
            two[ord(c) - ord('a')] +=1
        steps = 0
        for key in range(26):
            if one[key] <= two[key]:
                continue
            swap = 0
            while one[key] > two[key]:
                if two[swap] > one[swap]:
                    tmp = min(two[swap] - one[swap], one[key] - two[key])
                    steps += tmp
                    two[swap] -= tmp
                    two[key] += tmp
                swap+=1
        return steps
