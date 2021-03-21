class Solution {
public:
    int reverse(int x) {
        int ans=0;
        while(x){
            int mod=x%10;
            if (ans > INT_MAX/10 || (ans == INT_MAX / 10 && mod > 7)) return 0;
            if (ans < INT_MIN/10 || (ans == INT_MIN / 10 && mod < -8)) return 0;
            ans=10*ans+mod;
            x/=10;
        }
        return ans;
    }
};
