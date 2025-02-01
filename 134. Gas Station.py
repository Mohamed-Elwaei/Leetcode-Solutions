class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        residue = [gas[i] - cost[i] for i in range(len(gas))]

        if sum(residue) < 0:
            return -1
        
        

        totalCost=sum(cost)
        total=0
        start=0
        for i in range(len(cost)):
            total+=residue[i]
            if total < 0:
                start=i+1
                total=0
        return start
        
