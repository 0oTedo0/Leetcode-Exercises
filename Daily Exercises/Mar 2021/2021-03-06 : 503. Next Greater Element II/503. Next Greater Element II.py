class Solution:
    def nextGreaterElements(self, nums):
        n=len(nums)
        ans=[-1]*n
        stack=list()  # monotonic stack (decreasing)
        for i in range(2*n-1):
            next_one=i%n
            while(len(stack) and nums[next_one]>nums[stack[-1]]):  # Pop until the new element satisfies monoticity
                ans[stack[-1]]=nums[next_one]
                stack.pop()
            if ans[next_one]==-1:  # A trick to reduce time complexity. In other words, marked element will not be marked again.
                stack.append(next_one)
        return ans
