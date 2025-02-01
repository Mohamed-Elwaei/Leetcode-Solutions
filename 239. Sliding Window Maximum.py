from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = deque([])
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if r+1>=k:
                while q[0] < l:
                    q.popleft()
                l+=1
                output.append(nums[q[0]])
            r+=1
            # print(q)
        return output