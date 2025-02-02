class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        answer = prices[:]
        for i in range(len(prices)-1,-1,-1):
            while stack and stack[-1] > prices[i]:
                stack.pop()
            if stack: answer[i] -= stack[-1]
            stack.append((prices[i]))
        return answer
            