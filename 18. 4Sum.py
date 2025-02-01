def fourSum(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        seen = set()
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    lastNumber = target - nums[i] - nums[j] - nums[k]
                    if lastNumber in seen:
                        arr = sorted([nums[i], nums[j], nums[k], lastNumber])
                        ans.add((arr[0], arr[1], arr[2], arr[3]))
            seen.add(nums[i])
        return ans

    
nums = [1,0,-1,0,-2,2]
target = 0
print(fourSum(nums,target))