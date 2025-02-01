class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows=set()
        cols=set()

        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col]==0:
                    rows.add(row)
                    cols.add(col)

        for col in cols:
            for row in matrix:
                row[col]=0
        for row in rows:
            matrix[row]=[0]*len(matrix[row])                            