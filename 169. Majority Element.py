from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # My solution
        # majority=Counter(nums)
        # return majority.most_common(1)[0][0]
        #Optimal
        Majority=nums[0]
        count=1
        for n in nums[1:]:

            if n==Majority:
                count+=1
            elif n!=Majority:
                count-=1
            if count<0:
                Majority=n  
                count=1 
        return Majority         