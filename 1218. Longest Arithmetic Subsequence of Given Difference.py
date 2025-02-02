class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        #arr =    [1,2,3,4], difference = 1
        #longest= [1,2,3,4]

        #arr =     [1,5,7,8,5,3,4,2,1], difference = -2
        #longest = [1,1,1,1,2,3,1,2,4]

        mapping = {} #Map each element to the longest subsequence ending at the element
        for n in arr:
            mapping[n] = mapping.get(n - difference,0) + 1
        return max(mapping.values())