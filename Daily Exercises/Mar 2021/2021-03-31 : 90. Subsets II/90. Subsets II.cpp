class Solution {
public:
    vector<vector<int>> ans;
    vector<int> path;

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        dfs(nums,0);
        return ans;
    }
    void dfs(vector<int>& nums,int index){
        ans.push_back(path);
        for (int i = index; i < nums.size(); ++i) {
            if (i != index && nums[i] == nums[i - 1]) continue;
            path.push_back(nums[i]);
            dfs(nums,i+1);
            path.pop_back();
        }
    }
};
