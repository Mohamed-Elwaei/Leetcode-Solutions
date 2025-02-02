import math
class Solution(object):
    def Build_min_heap(self,points):
        for i in range(len(points)//2,-1,-1):
            self.min_heapify(points,i)
    def min_heapify(self,points,i):
        l=i*2
        r=(i*2)+1
        smallest=i
        if l<len(points) and self.radius(points[l])<self.radius(points[i]):
            smallest=l
        if r<len(points) and self.radius(points[r])<self.radius(points[smallest]):
            smallest=r
        if smallest!=i:
            points[i],points[smallest]=points[smallest],points[i]
            self.min_heapify(points,smallest)
    def extract_min(self,a):
        a[0],a[-1]=a[-1],a[0]
        ret=a.pop()
        self.min_heapify(a,0)
        return ret
    def priorityQ(self,a):
        ret=[]
        while len(a)>0:
            ret.append(self.extract_min(a))
        return ret

    def radius(self,point):
        return math.sqrt((point[0]**2)+(point[1]**2))
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        "Simple solutions using sorted in python"
        # points=sorted(points,key=lambda point:self.radius(point))
        # return points[:k]

        "Heapsort/ Priority Queue Solution"
        self.Build_min_heap(points)
        points=self.priorityQ(points)
        return points[:k]