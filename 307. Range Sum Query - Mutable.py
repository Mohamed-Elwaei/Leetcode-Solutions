class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        n = len(nums)
        self.T = [0] * (n+1)

        for i in range(n):
            self._update(i,nums[i])
        

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        delta = -self.sumRange(index,index) + val
        self._update(index,delta)
    
    def _update(self,index,val):
        index+=1

        while index < len(self.T):
            self.T[index] += val
            index += (index & -index)

    def prefixSum(self, index):
        index+=1

        ret = 0
        while index:
            ret+=self.T[index]
            index -= (index&-index)
        return ret



    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return self.prefixSum(right) - self.prefixSum(left-1)
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)