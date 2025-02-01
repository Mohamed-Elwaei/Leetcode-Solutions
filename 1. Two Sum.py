class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices=dict()

        for i,a in enumerate(nums):
            b=target-a

            if b in indices :
                for j in indices[b]:
                    if j!=i: 
                        return [i,j]
            
            if a in indices:
                indices[a].append(i)
            else:
                indices[a] = [i]
        