class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        def helper(x):
            while x - 1 in tmp: #Keep decrementing x till reaching the start of the sequence
                x -= 1 
            ret = 0
            while x in tmp: #Keep incrementing x till reaching the end. Remove x so as not to revisit it
                tmp.remove(x)
                ret += 1
                x += 1
            return ret

        tmp = set(nums)
        longest = 0 
        for n in nums:
            if n not in tmp:
                continue
            else:
                longest = max(helper(n), longest)
        return longest
        