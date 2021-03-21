class Solution {
    public int reverse(int x) {
        int ans=0;
        while(x!=0){
            int mod=x%10;
            if (ans > Integer.MAX_VALUE/10 || (ans == Integer.MAX_VALUE / 10 && mod > 7)) return 0;
            if (ans < Integer.MIN_VALUE/10 || (ans == Integer.MIN_VALUE / 10 && mod < -8)) return 0;
            ans=10*ans+mod;
            x/=10;
        }
        return ans;
    }
}
