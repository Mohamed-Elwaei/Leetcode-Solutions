class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        st = []
        ans = 0

        for i,n in enumerate(nums):
            if not st or nums[st[-1]]>n:
                st.append(i)
        for i in range(len(nums) - 1, -1, -1):
            while st and nums[i] >= nums[st[-1]]:
                ans = max(ans, i - st.pop())
        return ans