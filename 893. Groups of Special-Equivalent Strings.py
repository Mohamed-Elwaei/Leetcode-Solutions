"""
We will divide each word into two parts.

for each word w:
    first part is w0w2w4...
    second is w1w3w5....
    
    we will sort both parts so they are lexicographically smallest.

    we will pair them up in a tuple and insert them in a set.
    we will do that for each word.

we check the size of the set at the end.

"""

class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        pairs = set()
        
        for w in words:
            first = []
            second = []

            for i in range(len(w)):
                if i & 1:
                    second.append(w[i])
                else:
                    first.append(w[i])
            first.sort()
            second.sort()

            first = ''.join(first)
            second = ''.join(second)
            pairs.add((first, second))
        return len(pairs)