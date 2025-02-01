def jump(nums):


        n=len(nums)
        i=0
        steps=0
        maxLen = i
        while maxLen<n-1:
            for j in range(i, nums[i]+i):
                if nums[j]+j > maxLen:
                    bestIndex=j
                maxLen =max(nums[j] + j, maxLen)
            
            steps+=1
            i=bestIndex
        return steps+1



nums=[2,3,1,1,4]

print(jump(nums))