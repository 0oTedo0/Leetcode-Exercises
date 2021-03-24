class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n=nums.size();
        stack<int> s;
        s.push(nums[n-1]);
        int max_2=INT_MIN;
        for(int i=n-2;i>=0;i--){
            if(nums[i]<max_2){
                return true;
            }
            while(!s.empty() && nums[i]>s.top()){
                max_2=s.top();
                s.pop();
            }
            if(nums[i]>max_2){
                s.push(nums[i]);
            }
        }
        return false;
    }
};
