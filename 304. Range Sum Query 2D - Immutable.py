
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        rows,cols=len(matrix),len(matrix[0])
        self.T=[]

        for c in range(cols+1):
            self.T.append([0] * (rows+1))

        for r in range(1,rows+1):
            self.T[r][1] = matrix[r-1][0]
        for c in range(1,cols+1):
            self.T[1][c] = matrix[0][c-1]
        
        for r in range(1,rows+1):
            for c in range(1,cols+1):
                self.T[r][c] = self.T[r-1][c] + self.T[r][c-1] + matrix[r-1][c-1] - self.T[r-1][c-1]
        



        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.T[row2][col2] - self.T[row2][col1] - self.T[row1][col2]



matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
obj = NumMatrix(matrix)

calls = [[2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]

for c in calls:
    print(obj.sumRegion(c[0],c[1],c[2],c[3]))