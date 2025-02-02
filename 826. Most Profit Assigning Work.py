class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        def bs(w):
            l,r = 0, len(difficulty) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if difficulty[mid] > w:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        worker.sort()
        tmp = sorted(zip(difficulty, profit))
        difficulty = [i[0] for i in tmp]
        profit = [i[1] for i in tmp]
        ans = 0
        max_profit = 0  # Track the maximum profit for each difficulty level
        
        for w in worker:
            index = bs(w)
            if index > 0:
                max_profit = max(max_profit, max(profit[:index]))
            ans += max_profit
        
        return ans