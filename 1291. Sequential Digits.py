class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequential = []
        nums = [0,1,2,3,4,5,6,7,8,9]
        def dfs(num):
            if low<=num<=high:
                
                sequential.append(num)
            if num> high:
                return
            
            last = str(num)[-1]
            next = ord(last) - ord('0') + 1
            
            if next <= 9:
                dfs(num * 10 + next)
        for n in range(1,10):
            dfs(n)
        sequential.sort()
        return sequential