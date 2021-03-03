class NumArray:

    def __init__(self, nums):
        self.sums = [0]

        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, i, j):
        return self.sums[j + 1] - self.sums[i]
