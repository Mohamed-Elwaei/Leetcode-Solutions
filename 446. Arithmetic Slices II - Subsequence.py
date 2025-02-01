def numberOfArithmeticSlices( nums: [int]) -> int:
        def search(l, r, t):
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] == t:
                    return [mid, nums[mid]]
                elif nums[mid] > t:
                    r = mid - 1
                else:
                    l = mid + 1
            return [False,False]
        count = 0 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                seq = [nums[i],nums[j]]
                left,nxt = search(j, len(nums) -1, seq[-1] + (seq[-1] - seq[-2]))
                while left:
                    seq.append(nxt)
                    count+=1
                    print(seq)
                    left, nxt = search(left, len(nums) - 1 , seq[-1] + (seq[-1] - seq[-2]))
                    
        return count

nums = [2,4,6,8,10]
print(numberOfArithmeticSlices(nums))