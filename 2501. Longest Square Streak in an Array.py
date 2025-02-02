class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        #nums = [4,3,6,16,8,2]
        #sorted = [2,3,4,6,8,16]
                #   [3,1,2,1,1,1]
        nums.sort()

        longest = {}
        for n in nums[::-1]:
            longest[n] = longest.get(n*n,0) + 1
        
        answer = max(longest.values())
        if answer < 2:
            answer = -1
        return answer