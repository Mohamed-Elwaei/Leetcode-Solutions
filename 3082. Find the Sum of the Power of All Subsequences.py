class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        """
        nums = [1,2,3], k = 3 
        Subsequences with sum 3: [1,2], [3]
        2^(3 - 2) + 2^(3-1) = 6
        
        
        2 ^ leftover no.s
        
        Find all subsequences with sum K.
        For each subsequence:
            answer += 2 ^ (len(arr) - len(subsequence))
            
        Use dfs with backtracking to find all subsequences with sum K.
        
        
        nums = [5] * 100 k = 5
        
        answer += 2^99
        """
        
        def helper():
            nonlocal length, total, answer, M, N
            
            tmp = 1
            for _ in range(N - length):
                tmp = (tmp * 2) % M
            answer = (answer + tmp) % M
        
        nums.sort()
        N = len(nums)
        total = 0 #Sum of subsequence
        length = 0 #Length of subsequence
        answer = 0
        M = 10**9 + 7
        
        def dfs(index):
            nonlocal length, total, answer, M, N
            if total == k:
                helper()
                return 
            elif total > k:
                return 
            
            for i in range(index, N):
                total += nums[i]
                length += 1
                dfs(i + 1)
                total -= nums[i]
                length -= 1
        dfs(0)
        return answer
                
                
s = Solution()
print(s.sumOfPower([1,2,3],3))