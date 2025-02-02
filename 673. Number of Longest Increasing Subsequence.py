class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        LIS = [[1, 1] for _ in range(N)]  # Proper initialization

        for i in range(N):
            for j in range(i):
                if nums[j] >= nums[i]:
                    continue

                if LIS[j][0] + 1 > LIS[i][0]:
                    LIS[i] = [LIS[j][0] + 1, LIS[j][1]]
                elif LIS[j][0] + 1 == LIS[i][0]:
                    LIS[i][1] += LIS[j][1]

        longest = max(LIS, key=lambda x: x[0])[0]  # Find the length of the longest subsequence
        answer = 0
        for length, count in LIS:
            if length == longest:
                answer += count
        return answer