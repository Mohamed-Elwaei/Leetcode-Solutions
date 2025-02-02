class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        N = len(nums)
        """[1,2,3,4,5,6]

        F(2,[1,2]) = F(6,[3,4,5,6]) + F(4,[3,4,5,6])
        F(1,[1,2]) = F(6,[3,4,5,6]) + F(4,[3,4,5,6]) + F(3,[3,4,5,6]) + F(5,[3,4,5,6])
        
        States are revisited.
        State consists of leading num and all nums in array.
        We can store nums as a number (masking bits)
        """
        memo = {}
        N = len(nums)
        MOD = (10**9) + 7
        def dfs(leading, visited):
            state = (leading, visited)
            if state in memo:
                return memo[state]
            elif visited.bit_count() == N:
                return True
            memo[state] = 0
            for i in range(N):
                if (1 << i) & visited: continue
                if (nums[i] % leading == 0 or leading % nums[i] == 0):
                    memo[state] = (memo[state] + dfs(nums[i], visited | (1 << i))) % MOD
            return memo[state] % MOD
        
        return sum([dfs(nums[i], (1 << i)) for i in range(N)]) % MOD


        