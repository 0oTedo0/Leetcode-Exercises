class Solution {
    public boolean find132pattern(int[] nums) {
        int n=nums.length;
        Deque<Integer> s = new LinkedList<Integer>();
        s.push(nums[n-1]);
        int max_2=Integer.MIN_VALUE;
        for(int i=n-2;i>=0;i--){
            if(nums[i]<max_2){
                return true;
            }
            while(!s.isEmpty() && nums[i]>s.peek()){
                max_2=s.peek();
                s.pop();
            }
            if(nums[i]>max_2){
                s.push(nums[i]);
            }
        }
        return false;
    }
}
