class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangles=[]
        for n in range(1,rowIndex+2):
            row=[1]*n
            if len(row)>2:
                for i in range(1,len(row)-1):
                    row[i]=triangles[n-2][i]+triangles[n-2][i-1]
            triangles.append(row)
        return triangles[rowIndex] 