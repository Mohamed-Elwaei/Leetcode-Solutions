from collections import defaultdict
def pacificAtlantic( heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        points=dict()

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                points[(r,c)] = [False,False]
        rows,cols=len(heights),len(heights[0])

        def dfs(r,c, curr):
            if (r<0 or c<0 
                or r>=rows or c>=cols or
                heights[r][c] > curr):
                return False
            
            
            if r==0 or c==0:
                points[(r,c)][1] = True #Pacific block
            if r==rows-1 or c==cols-1:
                points[(r,c)][0] = True #Atlantic block
            
            if sum(points[(r,c)]) == 2:
                return True
            
            res=(
                dfs(r+1,c,heights[r][c]) or
                dfs(r,c+1,heights[r][c]))

            if res:
                points[(r,c)][1] = True
                points[(r,c)][0] = True
                return True
            return False
    

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                dfs(r,c,heights[r][c])


        res=[]
        for point in points:
            if sum(points[point])==2:
                res.append(point)
        return res
        
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

print(pacificAtlantic(heights))