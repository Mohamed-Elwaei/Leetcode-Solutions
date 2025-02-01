class Solution(object):

    def EEA(self,a,b):
        if b==0:
            return a,1,0 #GCD, y1, x1
        
        gcd,x1,y1=self.EEA(b,a%b)
        x=y1
        y=x1-(a//b)*y1
        return gcd,x1,y1

    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        if targetCapacity>(jug1Capacity+ jug2Capacity):
            return False

        if targetCapacity%self.EEA(jug1Capacity, jug2Capacity)[0]:
            return False
        return True