class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(index):
            if path not in ans:
                ans.append(deepcopy(path))
            for i in range(index, len(nums)):
                if i>index and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                dfs(i + 1)
                path.pop()

        ans = []
        path=[]
        nums.sort()
        dfs(0)
        return ans
