class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d=dict()
        n=len(nums)
        for i in range(n):
            if target-nums[i] in d:  # Find it in dictionary
                return [d[target-nums[i]],i]
            else:
                d[nums[i]]=i  # Record it
