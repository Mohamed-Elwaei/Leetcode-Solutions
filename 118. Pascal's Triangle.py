class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangles=[]
        for n in range(1,numRows+1):
            row=[1]*n
            if len(row)>2:
                for i in range(1,len(row)-1):
                    row[i]=triangles[n-2][i]+triangles[n-2][i-1]
            triangles.append(row)
        return triangles  
        return triangles    
        