class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a=[]
        for i in range(0,len(matrix)):
            a.extend(matrix[i])
        left=0
        right=len(a)-1
        while right>=left:
            mid=(left+right)//2
            if a[mid]==target:
                return True
            elif a[mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False
        

