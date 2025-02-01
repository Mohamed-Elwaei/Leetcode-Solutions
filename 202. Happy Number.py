class Solution:
    def isHappy(self, n: int) -> bool:
        pairs=set()

        while n!=1:
            digits=[]
            newnum=0
            while n>0:
                digit=n%10
                newnum+=digit**2
                digits.append(digit)
                n//=10
            if tuple(digits) in pairs:
                return False    
            pairs.add(tuple(digits))
            n=newnum   
        return True  