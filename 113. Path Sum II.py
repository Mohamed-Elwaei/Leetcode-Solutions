def wiggleSort( nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        ans=[]

        p,q=0,len(nums)-1

        turn=0
        while p<=q:
            if turn:
                ans.append(nums[q])
                q-=1
            else:
                ans.append(nums[p])
                p+=1
            turn^=1
        return ans

nums = [1,5,1,1,6,4]
print(wiggleSort(nums))