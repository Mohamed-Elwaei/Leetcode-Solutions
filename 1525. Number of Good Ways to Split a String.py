"""
Solution would be using 2 multisets, left, and right.

then we iterate over the array.

For c in s:
    left.add(c)
    right.remove(c)
    
    check both have the same no. of distinct characters.
    add 1 to the answer


"""

class Solution:
    def numSplits(self, s: str) -> int:
        left,right = {}, {}

        for c in s:
            right[c] = right.get(c,0) + 1
        

        answer = 0
        for c in s:
            left[c] = left.get(c,0) + 1
            right[c] -= 1
            if right[c] == 0:
                del right[c]
            
            if len(left) == len(right):
                answer += 1
        return answer
        