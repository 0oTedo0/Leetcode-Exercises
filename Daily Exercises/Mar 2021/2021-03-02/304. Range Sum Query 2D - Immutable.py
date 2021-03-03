class NumMatrix:
  
    def __init__(self, matrix):
        nrow=len(matrix)
        ncol=len(matrix[0]) if matrix else 0
        self.sums=[[0]*(n+1) for _ in range(m+1)]  # Initialization
        
        for i in range(m):
            for j in range(n):
                self.sums[i+1][j+1]=self.sums[i][j+1]+self.sums[i+1][j]-self.sums[i][j]+matrix[i][j]  # Compute the sum of all values from row 0->i and column 0->j

    def sumRegion(self, row1, col1, row2, col2):
        return self.sums[row2+1][col+1]-self.sums[row1][col2+1]-self.sums[row2+1][col1]+self.sums[row1][col1]  # Compute the sum of values by the same method above
      
      
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
