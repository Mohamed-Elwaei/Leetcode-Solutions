import string
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indices = {}
        for index,letter in enumerate(s):
            indices[letter] = indices.get(letter, []) + [index]
        start, end = indices[s[0]][0], indices[s[0]][-1]
        intervals = []
        for index,letter in enumerate(s):
            if index > end:
                intervals.append(end - start + 1)
                start, end = indices[s[index]][0], indices[s[index]][-1]
            else:
                end = max(indices[s[index]][-1], end)
        intervals.append(end - start + 1)
        return intervals 