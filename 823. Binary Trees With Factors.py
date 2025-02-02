class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        #[2,4]
        #[1,1]

        #[2,3,4,12] for 12: 12, dp[4] * dp[3], dp[3] * dp[4]
        #[1,1,2,5]

        def bs(right, target):
            l,r = 0,right
            while l <= r:
                mid = l + (r - l) // 2
                if arr[mid] > target: 
                    r = mid - 1
                elif arr[mid] < target:
                    l = mid + 1
                else:
                    return mid
            return l

        arr.sort()
        N = len(arr)
        M = (10**9) + 7
        dp = [1] * N
        for i in range(N):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    firstFactor, secondFactor = j, bs(i,arr[i] // arr[j])
                    if arr[firstFactor] * arr[secondFactor] == arr[i]:
                        dp[i] += (dp[firstFactor] * dp[secondFactor]) % M
        return sum(dp) % M
                        