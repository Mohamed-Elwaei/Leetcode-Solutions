class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        """
        1 <= N <= 10**5
        -100 <= nums[i] <= 100
        F(k) rotates k times clockwise.
        Return Max(F(k) for k from 0 to N-1)

        nums = [4,3,2,6]
        F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
        F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
        F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
        F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

        F(1) = F(0)(25) - 18 + 4 + 3 + 2 = F(0) - 18 + 9 = 25
        F(2) = F(1)(16) - 6 + 6 + 4 + 3 = F(1) - 6 + 13 = 23
        F(3) = F(2)(23) - 9 + 2 + 6 + 4 = F(2) - 9 + 12 = 26

        at F(k) We want to subtract (N - 1) * arr[N - 1 - (k - 1)]
        What should we add at F(k)?
        F(k) = F(k - 1) + total - (lastNum * N) - lastNum
        """
        N = len(nums)
        total = sum(nums)
        FKminusOne = sum([i * n for i,n in enumerate(nums)])
        answer = FKminusOne
        for k in range(1,N):
            lastNum = nums[N - 1 - (k - 1)]
            FK = FKminusOne + total - (N * lastNum)
            FKminusOne = FK
            answer = max(answer, FK)
        return answer