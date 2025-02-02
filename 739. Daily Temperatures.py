class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        ret=[0]*len(temperatures)
        stack=[]

        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][1]:
                tmp=stack.pop()
                ret[tmp[0]]=i-tmp[0]  
            stack.append([i,t])
        return ret    