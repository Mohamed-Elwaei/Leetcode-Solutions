def subsets( nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output=[]
        for i in range(2**(len(nums))):
            binary=bin(i)[::-1]
            subset=[]

            for i,c in enumerate(binary[:-2]):
                  if c=='1':
                        subset.append(nums[i])
            output.append(subset)
        return output
def subsets( nums):
        res = [[]]
        for num in sorted(nums):
            res += [item+[num] for item in res]
        return res

print(subsets([1,2,3]))