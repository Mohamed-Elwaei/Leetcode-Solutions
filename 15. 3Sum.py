class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        indices=dict()

        for i,n in enumerate(nums):
            if n in indices:
                indices[n].append(i)
            else:
                indices[n] = [i]

        triplets=set()
        for a in range(len(nums)):
            for b in range(a+1,len(nums)):
                c=-nums[a]-nums[b]
                if c in indices:
                    triplet=tuple(sorted([nums[a],nums[b],c]))
                    if triplet in triplets:
                        continue
                    for i in indices[c]:
                        if i!=a and i!=b:
                            triplets.add(triplet)
        return triplets
        