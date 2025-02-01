def twoSum( numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        p,q=0,len(numbers) -1
        currsum=numbers[p]+numbers[q]

        while target!=currsum and p<q:
            currsum=numbers[p]+numbers[q]
            if currsum>target:
                q-=1
            elif currsum<target:
                p+=1
            else:
                 return [p,q]
        return [p,q]

numbers = [2,7,11,15]
target = 9
print(twoSum(numbers,target))