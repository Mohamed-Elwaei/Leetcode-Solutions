class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        answer = nums[:]
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            answer[i] = -1 if not stack else stack[-1]
            stack.append(nums[i])
        print(answer)
        for i in range(len(nums)-1,-1,-1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()
            answer[i] = -1 if not stack else stack[-1]
            stack.append(nums[i])
        return answer
            