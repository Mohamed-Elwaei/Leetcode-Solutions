"""
if only one string has length equal to the max length, return the length of that string.
A trie would work for substrings, but not subsequences.

Each strs[i] has <= 10 letters.

So go through all 2^10 possible subsequences in each string and determine the largest.
"""
from collections import defaultdict
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        mapping = defaultdict(set)

        n = len(strs)

        def LUS(num): #if num's ith bit is set, pick the ith character in each string.

            for i in range(len(strs)):
                string = strs[i]
                flag = 0
                subsequence = ''
                for j in range(10):

                    if (1 << j) & num:
                        if j >= len(string):
                            flag = 1
                            break
                        else:
                            subsequence += string[j]
                if flag == 0:
                    mapping[subsequence].add(i)
            
                        
            



        for i in range(1, 2 << 10):
            LUS(i) 

        
        answer = -1

        for subsequence in mapping:
            if len(mapping[subsequence]) == 1:
                answer = max(answer, len(subsequence))
        return answer