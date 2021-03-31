class Solution {
    List<List<Integer>> ans=new ArrayList<List<Integer>>();
    List<Integer> path=new ArrayList<Integer>();
    
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        dfs(nums,0);
        return ans;
    }
    public void dfs(int[] nums,int index){
        if (index > nums.length) return;
        ans.add(new ArrayList<>(path));
        for (int i = index; i < nums.length; ++i) {
            if (i != index && nums[i] == nums[i - 1]) continue;
            path.add(nums[i]);
            dfs(nums,i+1);
            path.remove(path.size()-1);
        }
    }
}
