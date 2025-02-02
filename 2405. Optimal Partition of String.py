from collections import deque
class Solution:
    def partitionString(self, s: str) -> int:
        indices = {}#Letter => indices where it occurs in s
        for index, letter in enumerate(s):
            if letter in indices:
                indices[letter].append(index)
            else:
                indices[letter] = deque([index])
        start, end = -1, -1

        partitions = 0
        for letter in s:
            index = indices[letter].popleft()
            if index > end:
                start = index
                end = float('inf')
                partitions += 1
            if indices[letter]:
                end = min(end,indices[letter][0] - 1)
     
                
        return partitions