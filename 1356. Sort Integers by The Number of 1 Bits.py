class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        def countBits(n):
            ones = 0
            while n:
                n&=(n-1)
                ones+=1
            return ones
        
        return sorted(arr, key = lambda x: (countBits(x),x))
        