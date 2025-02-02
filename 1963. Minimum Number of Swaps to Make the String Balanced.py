class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = 0
        n = len(s)
        
        l = 0
        r = n - 1

        s = [c for c in s]
        left_side = 0
        right_side = 0
        while l < r:
            while l < r and left_side >= 0:
                if s[l] == '[':
                    left_side += 1
                else:
                    left_side -= 1
                if left_side == -1: break

                l += 1

            while l < r and right_side >= 0:
                if s[r] == ']':
                    right_side += 1
                else:
                    right_side -= 1
                if right_side == -1: break
                r -= 1
            
            if l < r:
                s[l],s[r] = '[', ']'
                swaps += 1
                right_side = left_side = 0
                
                
        return swaps