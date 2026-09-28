class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        a=[]
        for x,y in points:
            d=x*x+y*y
            heapq.heappush(heap,(d,x,y))
        for i in range(0,k):
            d,x,y=heapq.heappop(heap)
            a.append([x,y])
        return a
        
            

        

        