class NumArray:

    def __init__(self, nums):
        self.sums = [0]  # An array that contains prefix sum
                         # self.nums[i]=sum(nums[0:i])

        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, i, j):
        return self.sums[j + 1] - self.sums[i]

    
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
