import random
class DisjointSet:
    def __init__(self,size):
        self.parents=list(range(size))
        self.size=[0] * size

    
    def make_set(self, x):
         self.parents[x]=x
         self.size[x]=1
    

    def union(self,x,y):
         x,y=self.find(x), self.find(y)

         if x!=y:
            if (self.size[x] < self.size[y]):
                x,y=y,x
            self.parents[y]=x
            self.size[x]+=self.size[y]
    def find(self, a):
         if a!=self.parents[a]:
              self.parents[a]=self.find(self.parents[a])
         return self.parents[a]


def findCircleNum(isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        DSU=DisjointSet(len(isConnected))

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j]:
                    DSU.union(i,j)
        return len(DSU.size)




print(findCircleNum([[1,1,0],[1,1,0],[0,0,1]]))


        